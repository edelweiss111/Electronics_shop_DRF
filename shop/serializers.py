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
    """Сериализатор редактирования модели поставщика"""

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

        vendor = Vendor.objects.create(contacts=contacts, **validated_data)

        return vendor


class VendorUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления модели поставщика"""

    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ('arrears', 'date_added')

    def update(self, instance, validated_data):
        """Переопределение метода обновления"""
        products = validated_data.pop('products', None)
        contacts = validated_data.pop('contacts', None)

        if validated_data:
            try:
                instance.name = validated_data['name']
            except KeyError:
                pass
            try:
                instance.supplier = validated_data['supplier']
            except KeyError:
                pass
        if products:
            for product in products:
                instance.products.add(product)

        if contacts:
            instance.contacts = contacts

        instance.save()

        return instance
