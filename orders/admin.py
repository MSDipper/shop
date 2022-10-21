from django.contrib import admin

from orders.models import OrderItemList, Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItemList)
class OrderItemListAdmin(admin.ModelAdmin):
    pass

