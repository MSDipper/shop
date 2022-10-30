from django.urls import path
from orders.views import order_create, admin_order_detail


urlpatterns = [
    path('admin/order/<order_id>/', admin_order_detail, name='admin_order_detail'),
    path('create/', order_create, name='order_create'),
]