from django import template
from shop.models import Product
from django.db.models import Count


register = template.Library()


@register.simple_tag()
def get_products():
    return Product.objects.filter(published=True).select_related('color')