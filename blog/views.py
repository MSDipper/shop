from django.shortcuts import render
from blog.models import Post, Ip


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
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        post.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        post.views.add(Ip.objects.get(ip=ip))  
        
    context = {
        'post_list':post,
    }
    return render(request, 'blog/post_list.html', context)