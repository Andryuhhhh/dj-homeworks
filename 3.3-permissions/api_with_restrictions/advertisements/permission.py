from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # Это я для себя. Сюда входят кортеж безопасных методов GET, HEAD, OPTIONS
            return True
        return request.user == obj.creator