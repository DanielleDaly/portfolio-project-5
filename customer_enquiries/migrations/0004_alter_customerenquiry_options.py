# Generated by Django 3.2.25 on 2024-05-06 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_enquiries', '0003_customerenquiry_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerenquiry',
            options={'verbose_name_plural': 'Customer Enquiries'},
        ),
    ]