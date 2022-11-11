from django.urls import path
from shop.views import(
                    ShopListView,
                    ProductDetailView,
                    FilterProduct,
                    CreateComment,
                    AddReview,
                    AddStarRating,
                    GetCategoryProductListView,
                    )


urlpatterns = [
    path('filter/', FilterProduct.as_view(), name='filter_products'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path('category/<slug:slug>/', GetCategoryProductListView.as_view(), name='get_product_category'),    
    path('comment/<int:pk>/', CreateComment.as_view(), name="create_comment"), 
    path('<id>/<slug>', ProductDetailView.as_view(), name='product_single'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path('category_slug/',ShopListView.as_view(), name='product_list_by_category'),
    path('', ShopListView.as_view(), name='shop'),
]
