# Отображение списка статей
from django.views.generic import ListView

from order_app.models import Order


class OrdersListView(ListView):
    """
    класс - ArticleList
    """
    model = Order
    paginate_by = 10
    template_name = 'order_list.html'
    ordering = 'pk'

