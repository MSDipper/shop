from contextlib import redirect_stderr
from django.urls import path
from account.views import Register, PagesPage
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', PagesPage.as_view(), name='pages'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='account/register/login.html'), name='login'),
    path('register_user/', Register.as_view(), name='register')
]
