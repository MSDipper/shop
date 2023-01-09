from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    """ Модель обратной связи """
    address = models.CharField(verbose_name='Адрес', max_length=50)
    phone = PhoneNumberField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email', max_length=254)
    
    class Meta:
        verbose_name = 'Наши контакты'
        verbose_name_plural = 'Наши контакты'
        
    def __str__(self):
        return f'{self.address}'    