# Generated by Django 3.2.25 on 2024-05-01 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_num_pages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
