from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    ''' Заказы посетителей '''
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    company_name = models.CharField(max_length=150, verbose_name='Компания')
    phone = PhoneNumberField(verbose_name='Телефон')
    address = models.CharField(verbose_name='Адрес', max_length=150)
    city = models.CharField(verbose_name='Город', max_length=150)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
  
        
    def __str__(self):
        return self.first_name
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItemList(models.Model):
    ''' Данные заказчика '''
    order = models.OneToOneField(
        Order, 
        related_name='items', 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        verbose_name='Заказ'
        )
    product = models.ForeignKey(
        Product, 
        related_name='order_items',
        verbose_name='Продукт',
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        )
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Цена'
        )
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во')


    class Meta:
        verbose_name = 'Данные заказчика'
        verbose_name_plural = 'Данные заказчика'
       
        
    def __str__(self):
        return f'{self.product} - {self.order}'
    
    
    def get_cost(self):
        return self.price * self.quantity