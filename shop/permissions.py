from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Пользователь активный"""

    def has_object_permission(self, request, view, obj):
        return request.user.is_active
