from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Post
from shop.models import Product


class HomeListView(TemplateView):
    template_name = 'home/home_list.html'

    def get_queryset(self):
        return Product.objects.all().select_related('product')
    
    
class Search(ListView):
    paginate_by = 3
    
    def get_queryset(self):
        return Post.objects.filter(
            title__icontains=self.request.GET.get("q")
            ) or Product.objects.filter(
                title__icontains=self.request.GET.get("q")
                )
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
