from django.contrib import admin

from orders.models import OrderItemList


@admin.register(OrderItemList)
class OrderItemListAdmin(admin.ModelAdmin):
    pass

