from django.urls import path
from shop.views import(
                    ShopListView,
                    ProductDetailView,
                    FilterProduct,
                    CreateComment,
                    )


urlpatterns = [
    path('filter/', FilterProduct.as_view(), name='filter_products'),
    path('comment/<int:pk>/', CreateComment.as_view(), name="create_comment"),
    path('<id>/<slug>', ProductDetailView.as_view(), name='product_single'),
    path('category_slug/',ShopListView.as_view(), name='product_list_by_category'),
    path('', ShopListView.as_view(), name='shop'),
]
