from django.urls import path
from blog.views import PostListView, GetCategoryListView, blog_detail


urlpatterns = [
    path('category/<slug:slug>/', GetCategoryListView.as_view(), name='get_category'),    
    path('<slug:slug>/', blog_detail, name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]