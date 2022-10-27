from django.contrib import admin

from orders.models import OrderItemList, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItemList
    raw_id_fields = ['product']


# @admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company_name',
                    'phone', 'address', 'city', 'notes')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)