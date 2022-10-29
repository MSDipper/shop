from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    ''' Купон пользователя '''
    code = models.CharField(max_length=50, unique=True, verbose_name='Код с купона')
    valid_from = models.DateTimeField(verbose_name='Время действительности купона')
    valid_to = models.DateTimeField(verbose_name='Время недействительности купона')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Процент скидки купона')
    active = models.BooleanField(verbose_name='Активность купона')
    
    
    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'
        
    
    def __str__(self):
        return self.code
    