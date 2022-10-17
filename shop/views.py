from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shop.models import Product

class ShopListView(ListView):
    model = Product
    paginate_by = 3
    template_name = 'shop/shop_list.html'
    
    

class ShopDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    slug_url_kwarg = 'slug'
    template_name = 'shop/shop_detail.html'