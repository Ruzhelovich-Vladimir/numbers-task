from django.apps import AppConfig


class OrderAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_app'
    verbose_name = "Приложение заказов"  # А здесь, имя которое необходимо отобразить в админке

    # def ready(self):
    #
    #     from . import signals
