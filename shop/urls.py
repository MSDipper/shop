from django.urls import path
from shop.views import ShopListView, product_detail


urlpatterns = [
    path('<id>/<slug>', product_detail, name='product_single'),
    path('category_slug/',ShopListView.as_view(), name='product_list_by_category'),
    path('', ShopListView.as_view(), name='shop'),
]
