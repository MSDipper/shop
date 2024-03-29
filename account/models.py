from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """ Вход пользователей через Email """
    email = models.EmailField(
        _('email address'),
        unique=True,
        )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']