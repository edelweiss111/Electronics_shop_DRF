# Generated by Django 5.0.3 on 2024-03-16 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_vendor_products_vendor_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='contacts',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.contact', verbose_name='Контакты'),
        ),
    ]
