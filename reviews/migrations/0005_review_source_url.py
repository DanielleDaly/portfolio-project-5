# Generated by Django 3.2.25 on 2024-05-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='source_url',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
