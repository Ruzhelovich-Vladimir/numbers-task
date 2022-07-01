from django.db import models


class Order(models.Model):
    """" Модель заказов """

    class Meta:
        verbose_name_plural = 'заказы'
        verbose_name = 'заказ'

    order_no = models.PositiveIntegerField(verbose_name='номер заказа', unique=True)
    usd_cost = models.DecimalField(verbose_name='сумма в долларах', default=0, max_digits=9, decimal_places=2)
    rub_cost = models.DecimalField(verbose_name='сумма в рублях', default=0, max_digits=9, decimal_places=2)
    delivery_day = models.DateField(verbose_name='срок поставки')

    def __str__(self):
        return f'id-{self.id}, order_no - {self.order_no}, ' \
               f'usd_cost - {self.usd_cost}, rub_cost - {self.rub_cost}, delivery_day - {self.delivery_day}'

