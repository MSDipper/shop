from django.urls import path
from contact.views import ContactListView


urlpatterns = [
    path('', ContactListView.as_view(), name='contact')
]
