from django.urls import path
from blog.views import PostListView, blog_detail


urlpatterns = [
    path('<slug:slug>/', blog_detail, name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]