# Generated by Django 3.2.25 on 2024-04-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240430_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_in_hardback',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
