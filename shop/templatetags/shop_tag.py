from django import template
from shop.models import Category, WeekProduct
from django.db.models import Count


register = template.Library()


@register.simple_tag()
def get_list_categories():
    return Category.objects.annotate(category_count=Count('product')).all() 


@register.simple_tag()
def get_week_product():
    return WeekProduct.objects.all() 