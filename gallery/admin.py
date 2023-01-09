from django.contrib import admin
from django.utils.safestring import mark_safe
from gallery.models import MyLife, ImageStyleLife


@admin.register(MyLife)
class MyLifeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter  = ['title']
    search_fields  = ['title']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="52" height="58">')
    
    get_image.short_description = "Изображение"


@admin.register(ImageStyleLife)
class ImageStyleLifeAdmin(admin.ModelAdmin):
    list_display = ['image', 'get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="48">')
    
    get_image.short_description = "Изображение"
