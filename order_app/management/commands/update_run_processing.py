""" Команда запуска процесса обновления базы.
Думал использовать django-celery-beat 2.3.0, но потом отказался из-за излишних наворотов
"""

import schedule
import time
from threading import Thread

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from google_api.api import get_data
from order_app.get_currency import get_currency
from order_app.models import Order

DAEMON = True  # фоновый режим запуска

def run_update():
    """ Запуск процесса по расписанию """
    # 1. получаем данные
    data = get_data()
    # 2. удаляем не нужные записи
    orders = Order.objects.all()
    for order in orders:
        delete_flag = True
        for date_order in data:
            if date_order["id"] == order.id:
                delete_flag = False
                break
        if delete_flag:
            order.delete()
    # 2. добавляем/обновляем запись
    for row in data:
        _id = row['id']
        _order_no = row['order_no']
        _usd_cost = row['usd_cost']
        _delivery_day = row['delivery_day']
        _currency = get_currency(_delivery_day)  # Получаем курс валюты
        _rub_cost = float(_usd_cost) * _currency
        row['rub_cost'] = _rub_cost

        try:
            # Попытка найти заказ по идентификатору
            order = Order.objects.get(pk=_id)
            # Если хоть одно поле изменилось, то запись обновляем
            if (order.order_no != _order_no) \
                    or (order.usd_cost != _usd_cost) \
                    or (order.rub_cost != _rub_cost) \
                    or (order.delivery_day != _delivery_day):
                order.order_no = _order_no
                order.usd_cost = _usd_cost
                order.rub_cost = _rub_cost
                order.delivery_day = _delivery_day
                order.save()
        except ObjectDoesNotExist:
            # Создаём запись
            Order.objects.create(**row)


def run_process():
    """ Цикл ожидания """
    while True:
        schedule.run_pending()
        time.sleep(1)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        schedule.every(15).seconds.do(run_update)
        th = Thread(target=run_process, daemon=DAEMON, name="update data")
        th.start()
