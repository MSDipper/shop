from django.urls import path
from home.views import Search, HomeListView


urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
]
