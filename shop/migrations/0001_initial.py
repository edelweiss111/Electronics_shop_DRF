# Generated by Django 5.0.3 on 2024-03-15 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, verbose_name='Почта')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house_number', models.PositiveIntegerField(verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('model', models.CharField(blank=True, max_length=50, null=True, verbose_name='Модель')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выхода на рынок')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('arrears', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='Задолженность перед поставщиком')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.contact', verbose_name='Контакты')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Продукты')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.vendor', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]