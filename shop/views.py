from django.shortcuts import render
from django.views.generic import ListView
from shop.models import Product

class ShopListView(ListView):
    model = Product
    paginate_by = 3
    template_name = 'shop/shop_list.html'