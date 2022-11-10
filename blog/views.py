from django.views.generic import ListView
from django.shortcuts import render
from blog.models import Post, Ip, Category
from django.shortcuts import get_object_or_404
from django.db.models import Count


def get_client_ip(request):
    ''' Просмотры '''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') 
    return ip


class PostListView(ListView):
    model = Post
    paginate_by = 3
    

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.annotate(category_count=Count('post'))
    
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        post.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        post.views.add(Ip.objects.get(ip=ip)) 
        
    context = {
        'post':post,
        'categories':categories,
    }
    return render(request, 'blog/post_detail.html', context)


class GetCategoryListView(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')
    