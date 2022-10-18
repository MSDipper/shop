from django.urls import path
from cart.views import cart_detail, cart_add, cart_remove


urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/', cart_add, name='cart_add'),
    path('remove/', cart_remove, name='cart_remove'),
]