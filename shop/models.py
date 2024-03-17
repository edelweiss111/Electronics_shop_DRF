from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель - продукта"""

    name = models.CharField(max_length=30, verbose_name='Название')
    model = models.CharField(max_length=50, **NULLABLE, verbose_name='Модель')
    release_date = models.DateField(**NULLABLE, verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс отображения метаданных"""
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Contact(models.Model):
    """Модель - контакты"""
    email = models.EmailField(max_length=150, verbose_name='Почта')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.PositiveIntegerField(verbose_name='Номер дома')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        """Класс отображения метаданных"""
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Vendor(models.Model):
    """Модель - поставщик"""

    name = models.CharField(max_length=30, verbose_name='Название')
    contacts = models.OneToOneField('Contact', **NULLABLE, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField('Product', verbose_name='Продукты')
    supplier = models.ForeignKey('Vendor', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    arrears = models.DecimalField(max_digits=11, decimal_places=2, **NULLABLE, verbose_name='Задолженность перед поставщиком')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    hierarchy_level = models.SmallIntegerField(default=0, **NULLABLE, verbose_name='Уровень иерархии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс отображения метаданных"""
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
