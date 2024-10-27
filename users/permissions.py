from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """
    Класс для разрешения доступа только клиентам с группой "moders"
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()
