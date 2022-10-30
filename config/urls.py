from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('coupons/', include('coupons.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)