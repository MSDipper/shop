from django.shortcuts import render
from blog.models import Post, Ip
from django.shortcuts import get_object_or_404

def get_client_ip(request):
    ''' Просмотры '''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') 
    return ip


def blog(request):
    post = Post.objects.all()
        
    context = {
        'post_list':post,
    }
    return render(request, 'blog/post_list.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        post.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        post.views.add(Ip.objects.get(ip=ip)) 
        
    context = {
        'post':post,
    }
    return render(request, 'blog/post_detail.html', context)