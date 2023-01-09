from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email']
    list_filter  = ( 'address', 'phone', 'email')
    search_fields  = ( 'address' , 'phone', 'email')
    save_as = True
    save_on_top = True