from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post
from shop.models import Product

class Search(ListView):
    paginate_by = 3
    
    def get_queryset(self):
         post = Post.objects.filter(title__icontains=self.request.GET.get("q"))
         product = Product.objects.filter(title__icontains=self.request.GET.get("q"))
         return post, product
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context