from django.urls import path
from coupons.views import coupon_apply


urlpatterns = [
    path('apply/', coupon_apply, name='apply'),
]