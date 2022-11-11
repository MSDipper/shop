from django.views.generic import ListView
from django.shortcuts import render, redirect
from blog.models import Post, Ip, Category
from django.shortcuts import get_object_or_404
from django.db.models import Count
from blog.forms import CommentPostForm
from django.views.generic.base import View


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
    
    def get_queryset(self):
        return Post.objects.all().select_related('author').select_related('category')
    

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.annotate(category_count=Count('post'))
    
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        post.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        post.views.add(Ip.objects.get(ip=ip)) 
    
    form = CommentPostForm()
    context = {
        'form':form,
        'post':post,
        'categories':categories,
    }
    return render(request, 'blog/post_detail.html', context)


class GetCategoryListView(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class GetTagListView(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(tag__slug=self.kwargs.get('slug')).prefetch_related('tag')
    

class SearchPost(ListView):
    paginate_by = 3
    
    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("q"))


class AddComment(View):
    """ Отправка коммента """
    def post(self, request, pk):
        form = CommentPostForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())