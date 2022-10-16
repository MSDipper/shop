from django.contrib import admin

from shop.models import Category, Brand, Specification, ImageProduct, Product, Comment, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    save_as = True
    save_on_top = True

admin.site.register(Specification)
admin.site.register(ImageProduct)
admin.site.register(Comment)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)