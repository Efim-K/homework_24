from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """
    Класс для разрешения доступа только клиентам с группой "moders"
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """
    Класс для разрешения доступа только клиентам владельцам
    """

    def has_object_permission(self, request, view, object):
        if object.owner == request.user:
            return True
        return False
