from django.urls import path
from blog.views import PostListView, GetCategoryListView, GetTagListView, blog_detail


urlpatterns = [
    path('tag/<slug:slug>/', GetTagListView.as_view(), name='get_tag'),    
    path('category/<slug:slug>/', GetCategoryListView.as_view(), name='get_category'),    
    path('<slug:slug>/', blog_detail, name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]