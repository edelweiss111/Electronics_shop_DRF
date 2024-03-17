from shop.apps import ShopConfig
from rest_framework.routers import DefaultRouter

from shop.views import VendorViewSet, ProductViewSet, ContactViewSet

app_name = ShopConfig.name
router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'contacts', ContactViewSet, basename='contact')


urlpatterns = [

] + router.urls
