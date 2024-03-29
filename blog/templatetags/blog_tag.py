from django import template
from blog.models import Category, Tag
from django.db.models import Count


register = template.Library()


@register.simple_tag()
def get_list_categories():
    return Category.objects.annotate(category_count=Count('post'))

@register.simple_tag()
def get_tags():
    return Tag.objects.all()