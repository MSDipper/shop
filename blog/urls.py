from django.urls import path
from blog.views import( 
                    PostListView,
                    GetCategoryListView, 
                    GetTagListView, 
                    SearchPost,
                    AddComment,
                    blog_detail
                    )


urlpatterns = [
    path('comments/<int:pk>/', AddComment.as_view(), name='add_comment'),
    path('search_post/', SearchPost.as_view(), name='search_post'),
    path('tag/<slug:slug>/', GetTagListView.as_view(), name='get_tag'),    
    path('category/<slug:slug>/', GetCategoryListView.as_view(), name='get_category'),    
    path('<slug:slug>/', blog_detail, name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]