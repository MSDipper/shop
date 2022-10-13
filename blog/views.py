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

        
    context = {
        'post_list':post,
    }
    return render(request, 'blog/post_list.html', context)