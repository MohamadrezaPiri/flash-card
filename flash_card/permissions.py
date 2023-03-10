from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        return bool(
            user and user.is_staff
            or
            user and user == obj.user
        )

    def has_permission(self, request, view):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        return bool(user and user.is_authenticated)
