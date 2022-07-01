from django.db.models.signals import pre_init,pre_save
from django.dispatch import receiver


from .get_currency import get_currency
from .models import Order


@receiver(pre_init, sender=Order)
@receiver(pre_save, sender=Order)
def pre_save_order_handler(sender, instance, *args, **kwargs):
    """ Добавление в статистику количество комментариев """

    _id = instance.id
    _order_no = instance.order_no
    _usd_cost = instance.usd_cost
    _rub_cost = instance.rub_cost
    _delivery_day = instance.delivery_day

    _currency = get_currency(_delivery_day)
    _rub_cost_new = float(_usd_cost) * _currency
    if _rub_cost != _rub_cost_new:
        instance.rub_cost = _rub_cost_new




