from rest_framework import permissions

class IsOwnerOrDeny(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
    Custom permission to only allow owners of an object to view/edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        else:
            return False