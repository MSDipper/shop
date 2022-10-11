from django.shortcuts import render
from blog.models import Post


def blog(request):
    post_list = Post.objects.all()
    context = {
        'post_list':post_list,
    }
    return render(request, 'blog/post_list.html', context)