from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from shop.models import Vendor, Product, Contact


def linkify(field_name):
    """
    Преобразует значение внешнего ключа в кликабельную ссылку.
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return '-'
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify


@admin.action(description='Очистить задолженность')
def clear_the_arrears(modeladmin, request, queryset):
    queryset.update(arrears=0)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """Админка отображения модели Vendor"""
    list_display = ('id', 'name', linkify(field_name="supplier"),)
    actions = [clear_the_arrears]
    list_filter = ('contacts__city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка отображения модели Product"""
    list_display = ('id', 'name', 'model', 'release_date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Админка отображения модели Contact"""
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number')
