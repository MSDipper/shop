from contextlib import redirect_stderr
from django.urls import path
from account.views import RegisterUser, PagesPage
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='account/register/login.html'), name='login'),
    path('register_user/', RegisterUser.as_view(), name='register'),
    path('', PagesPage.as_view(), name='pages'),
]
