from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe
from shop.models import (
                        Category,
                        Brand,
                        Specification,
                        Color,
                        ImageProduct,
                        Product,
                        Comment,
                        RatingStar,
                        Rating,
                        Reviews,
                        WeekProduct
                        )


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'slug', 'parent']
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['name']
    save_as = True
    save_on_top = True


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'main_image', 'get_image', 'price', 'create_at', 'quantity', 'availibility', 'published']
    list_filter  = ( 'title', 'category', 'price', 'create_at')
    search_fields  = ( 'title' , 'category__name')
    prepopulated_fields = {'slug': ('title',), }
    save_as = True
    save_on_top = True
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="50" height="48">')
    
    get_image.short_description = "Изображение"


@admin.register(WeekProduct)
class WeekProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "old_price", "image",)


@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    list_display = ("image", 'get_image',)
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="48">')
    
    get_image.short_description = "Изображение"

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'parent', 'photo', 'publish')
    list_filter  = ( 'name', 'parent', 'publish')
    search_fields  = ('name',)
    
  
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
