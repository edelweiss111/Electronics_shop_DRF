from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Electronic Network API Documentation",
        default_version='v1',
        description="Documentation for electronic sales network.",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('users/', include('users.urls', namespace='users')),
]
