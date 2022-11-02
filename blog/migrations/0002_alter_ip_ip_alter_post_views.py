# Generated by Django 4.1.2 on 2022-11-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, default=[0], null=True, related_name='post_views', to='blog.ip', verbose_name='Просмотры'),
        ),
    ]
