from django.contrib import admin
from django.urls import path, include

from order_app.views import OrdersListView

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders')
]
