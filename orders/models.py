from tabnanny import verbose
from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon


class Order(models.Model):
    ''' Данные заказчика '''
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    company_name = models.CharField(max_length=150, verbose_name='Компания')
    phone = PhoneNumberField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email', max_length=254, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=150)
    city = models.CharField(verbose_name='Город', max_length=150)
    notes = models.TextField(
        max_length=500, 
        verbose_name='Примечания к заказу',
        null=True,
        blank=True
        )
    coupon = models.ForeignKey(Coupon,
                                related_name='orders',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='Купон'
                                )
    discount = models.IntegerField(default=0,
                                verbose_name='Процент скидки купона',
                                validators=[MinValueValidator(0),
                                            MaxValueValidator(100)]
                                    )
    

    class Meta:
        verbose_name = 'Данные заказчика'
        verbose_name_plural = 'Данные заказчика'
  
        
    def __str__(self):
        return self.first_name
    
    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))
    

class OrderItemList(models.Model):
    ''' Заказы посетителей '''
    order = models.ForeignKey(
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
        )
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Цена'
        )
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
       
        
    def __str__(self):
        return f'{self.product} - {self.order}'
    
    
    def get_cost(self):
        return self.price * self.quantity