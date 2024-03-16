from rest_framework.permissions import BasePermission, SAFE_METHODS


class CanEditOrDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in SAFE_METHODS:
            return True

        # Allow editing and deleting for admin users
        if request.user.is_staff:
            return True

        # Allow editing and deleting for the client who made the post
        return obj.author == request.user.id