from django.urls import path
from shop.views import(
                    ShopListView,
                    product_detail,
                    FilterProduct,
                    )


urlpatterns = [
    path('filter/', FilterProduct.as_view(), name='filter_products'),
    path('<id>/<slug>', product_detail, name='product_single'),
    path('category_slug/',ShopListView.as_view(), name='product_list_by_category'),
    path('', ShopListView.as_view(), name='shop'),
]
