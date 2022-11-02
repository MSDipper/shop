from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    """ Категория """
    name = models.CharField(max_length=150, verbose_name='Имя')
    slug = models.SlugField(max_length=150, verbose_name='URL', unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
        )
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
        
    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])
    
    
    def __str__(self):
        return self.name        
          
        
class Brand(models.Model):
    """ Бренд """
    name = models.CharField(max_length=150, verbose_name='Имя')
    slug = models.SlugField(max_length=150, verbose_name='URL', unique=True)
    

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        
    def __str__(self):
        return self.name
        
        
class Specification(models.Model):
    """ Характеристика """
    name = models.CharField(verbose_name='Название', max_length=150, blank=True, null=True)
    width = models.IntegerField(verbose_name='Ширина')
    height = models.IntegerField(verbose_name='Высота')
    depth = models.IntegerField(verbose_name='Глубина')
    weight = models.IntegerField(verbose_name='Масса')
    quality_checking = models.CharField(max_length=150, verbose_name='Проверка качества')
    freshness_duration = models.IntegerField(verbose_name='Свежесть')
    when_packeting = models.CharField(max_length=150, verbose_name='При упаковке')
    

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        
        
    def __str__(self):
        return f'{self.name}'  


class ImageProduct(models.Model):
    """ Изображение """
    image = models.ImageField(upload_to='images/', verbose_name='Изображения к продукту')
    
    
    class Meta:
        verbose_name = 'Изображение к продукту'
        verbose_name_plural = 'Изображения к продукту'


    def __str__(self):
        return f'{self.image}'
    
    
class Product(models.Model):
    """ Товар """
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)
    old_price = models.DecimalField(verbose_name='Старая цена', max_digits=6, decimal_places=2)
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    create_at = models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)
    availibility = models.CharField(verbose_name='Статус доступности', max_length=50)
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    main_image = models.ImageField(upload_to='images/', verbose_name='Главное изображение продукта', null=True)
    slug = models.SlugField(max_length=150, verbose_name='URL', unique=True, null=True)
    description = RichTextField(verbose_name='Описание')
    category = models.ForeignKey(
        Category, 
        related_name='product',
        verbose_name='Категория',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
        )
    brand = models.ManyToManyField(
        Brand,
        related_name='product',
        verbose_name='Бренд'
        )
    specification = models.ManyToManyField(
        Specification, 
        related_name='product',
        verbose_name='Характеристики'
        )
    imageproduct = models.ManyToManyField(
        ImageProduct, 
        related_name='product',
        verbose_name='Изображения'
        )
    
    
    class Meta:
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
        
    def __str__(self):
        return self.title
    
        
    def get_absolute_url(self):
        return reverse('product_single', args=[self.id, self.slug])
    

class Comment(models.Model):
    """ Комментарии """
    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(max_length=254)
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(verbose_name='Фото', upload_to='photo/', blank=True, null=True)
    message = models.TextField(max_length=500, verbose_name='Текст')
    product = models.ForeignKey(
        Product, 
        related_name='comment', 
        verbose_name='Комментарий',
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    parent = models.ForeignKey(
        'self',
        verbose_name="Родитель",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
        
    def __str__(self):
        return f'{self.name} - {self.email}'    


class RatingStar(models.Model):
    """ Звезда рейтинга """
    value = models.SmallIntegerField("Значение", default=0)


    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]
        
        
    def __str__(self):
        return f'{self.value}'    
        
        
        
class Rating(models.Model):
    """ Рейтинг """
    ip = models.CharField("IP адрес", max_length=25)
    star = models.ForeignKey(RatingStar, verbose_name="Звезда", on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE, related_name="rating")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"   
    

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    message = models.TextField("Сообщение", max_length=500)
    parent = models.ForeignKey(
        'self',
        verbose_name="Родитель",
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    product = models.ForeignKey(
        Product,
        verbose_name="Продукт",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"