from django.urls import path
from shop.views import ShopListView, ShopDetailView

urlpatterns = [
    path('<slug:slug>/', ShopDetailView.as_view(), name='product_single'),
    path('', ShopListView.as_view(), name='shop'),
]
