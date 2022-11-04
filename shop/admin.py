from django.contrib import admin
from mptt.admin import MPTTModelAdmin
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
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True


@admin.register(Color)
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
admin.site.register(WeekProduct)
admin.site.register(ImageProduct)
admin.site.register(Comment)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
