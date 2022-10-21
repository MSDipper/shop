from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class OrderItemList(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    company_name = models.CharField(max_length=150, verbose_name='Компания')
    phone = PhoneNumberField(verbose_name='Телефон')
    address = models.CharField(verbose_name='Адрес', max_length=150)
    city = models.CharField(verbose_name='Город', max_length=150)

    class Meta:
        verbose_name = 'Данные заказчика'
        verbose_name_plural = 'Данные заказчика'
        
    def __str__(self):
        return self.first_name
    