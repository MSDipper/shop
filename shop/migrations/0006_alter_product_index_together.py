# Generated by Django 4.1.2 on 2022-10-18 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_description'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
