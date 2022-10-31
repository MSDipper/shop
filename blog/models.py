from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    slug = models.SlugField(max_length=200, verbose_name='URL', unique=True)
    

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.name


class Ip(models.Model): 
    ip = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IP'

    def __str__(self):
        return f'{self.ip}'


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    description = RichTextField(verbose_name='Описание')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    views = models.ManyToManyField(Ip, related_name="post_views", verbose_name='Просмотры', default=0)
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
        )
    category = models.ForeignKey(
        Category, 
        related_name='post',
        verbose_name='Категория',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
        )
    tag = models.ManyToManyField(Tag, related_name='post', verbose_name='Тег')
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
    def __str__(self):
        return self.title
    
    def total_views(self):
        ''' Счётчик просмотров '''
        return self.views.count()
    

    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(max_length=254)
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(verbose_name='Фото', upload_to='photo/', blank=True, null=True)
    message = models.TextField(max_length=500, verbose_name='Текст')
    post = models.ForeignKey(Post, related_name='comment', verbose_name='Комментарий', on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
    def __str__(self):
        return f'{self.name} - {self.email}'
    