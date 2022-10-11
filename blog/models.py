from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    slug = models.SlugField(max_length=200, verbose_name='URL', unique=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'



class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Ip(models.Model): 
    ip = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.ip}'
    
    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IP'



class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    mini_image = models.ImageField(upload_to='image_mini/', verbose_name='Мини изображение')
    description = RichTextField(verbose_name='Описание')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    views = models.ManyToManyField(Tag, verbose_name='Просмотры')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL')
    category = models.ForeignKey(
        Category, 
        related_name='post',
        verbose_name='Категория',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
        )
    tag = models.ManyToManyField(Tag, related_name='tag', verbose_name='Тег')
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(max_length=254)
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(verbose_name='Фото', upload_to='photo/', blank=True, null=True)
    message = models.TextField(max_length=500, verbose_name='Текст')
    post = models.ForeignKey(Post, related_name='comment', verbose_name='Комментарий', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'