from django.urls import path
from blog.views import blog, blog_detail


urlpatterns = [
    path('<slug:slug>/', blog_detail, name='post_detail'),
    path('', blog, name='post_list'),
]