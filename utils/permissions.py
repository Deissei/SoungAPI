from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsMyPlaylist(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff == True:
            return IsAdminUser
        return bool(obj.username == request.user.username)