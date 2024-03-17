from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from shop.models import Vendor, Product, Contact
from shop.serializers import VendorSerializer, VendorCreateSerializer, VendorUpdateSerializer, ProductSerializer, \
    ContactSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException


class VendorViewSet(viewsets.ModelViewSet):
    """Вьюсет модели поставщика"""
    queryset = Vendor.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contacts__country',)

    def destroy(self, request, *args, **kwargs):
        """Удаление продукта (в тело запроса передать 'products': [id продуктов]
        или поставищка (ничего не передавать)"""
        vendor = self.get_object()
        try:
            products = request.data['products']
            try:
                for product in products:
                    try:
                        obj = Product.objects.get(pk=product)
                        vendor.products.remove(obj)
                    except ValueError:
                        raise APIException('Ожидается список id продуктов')
                return Response(status=status.HTTP_200_OK)
            except TypeError:
                raise APIException('Ожидается список id продуктов')
        except KeyError:
            self.perform_destroy(vendor)
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от метода"""
        method = self.request.method
        if method == 'POST':
            return VendorCreateSerializer
        elif method == 'PATCH' or method == 'PUT':
            return VendorUpdateSerializer
        else:
            return VendorSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет модели продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """Вьюсет модели контактов"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
