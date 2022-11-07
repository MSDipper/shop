from django.db import models


class MyLife(models.Model):
    ''' О жизни '''
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    text = models.TextField(verbose_name='Текст')
    
    
    class Meta:
        verbose_name = 'Моя жизнь'
        verbose_name_plural = 'Моя жизнь'
        
        
    def __str__(self):
        return f'{self.title}'


class ImageStyleLife(models.Model):
    ''' Моя Галерея '''
    image = models.ImageField(
        upload_to='image_style_life/',
        blank=True,
        verbose_name='Фото'
        )
    
    
    class Meta:
        verbose_name = 'Мой стиль'
        verbose_name_plural = 'Мой стиль'
        
        
    def __str__(self):
        return f'{self.image}'