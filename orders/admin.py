from django.contrib import admin
from orders.models import OrderItemList, Order
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    ''' Скачивание файлов в формате csv '''
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Напишите первую строку с информацией заголовка
    writer.writerow([field.verbose_name for field in fields])
    # Запись строк данных
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItemList
    raw_name_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company_name',
                    'phone', 'email', 'address', 'city', 'notes')
    inlines = [OrderItemInline]
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)