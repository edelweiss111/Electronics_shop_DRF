from rest_framework import serializers

from shop.models import Vendor, Product, Contact


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели продукта"""

    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор модели контактов"""

    class Meta:
        model = Contact
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    """Сериализатор модели поставщика"""

    products = ProductSerializer(many=True)
    contacts = ContactSerializer(many=False)

    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ('arrears', 'date_added')


class VendorCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания модели поставщика"""

    contacts = ContactSerializer(many=False)

    class Meta:
        model = Vendor
        fields = ('name', 'supplier', 'arrears', 'contacts')

    def create(self, validated_data):
        """Создание объекта поставщика вместе с контактными данными"""
        contacts_data = validated_data.pop('contacts')
        contacts = Contact.objects.create(**contacts_data)
        # Вычисление уровня иерархии
        try:
            supplier = validated_data['supplier']
            hierarchy_level = supplier.hierarchy_level + 1
            vendor = Vendor.objects.create(contacts=contacts, hierarchy_level=hierarchy_level, **validated_data)
        except KeyError:
            vendor = Vendor.objects.create(contacts=contacts, **validated_data)

        return vendor


class VendorUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления модели поставщика"""

    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ('arrears', 'date_added', 'hierarchy_level')

    def update(self, instance, validated_data):
        """Переопределение метода обновления"""
        products = validated_data.pop('products', None)
        contacts = validated_data.pop('contacts', None)

        # Сохранение полей name, supplier, если они передаются, смена значения уровня иерархии
        if validated_data:
            try:
                instance.name = validated_data['name']
            except KeyError:
                pass
            try:
                supplier = validated_data['supplier']
                instance.supplier = supplier
                instance.hierarchy_level = supplier.hierarchy_level + 1
            except KeyError:
                pass
        # Сохранение продуктов
        if products:
            for product in products:
                instance.products.add(product)
        # Сохранение контактов
        if contacts:
            # instance.contacts.delete()
            instance.contacts = contacts

        instance.save()

        return instance
