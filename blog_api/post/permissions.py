
from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostPermissions(BasePermission):
    """
    Permissions for posts.
    Allow to retrieve posts for everyone
    Allow post creation only for authenticated users.
    Post modification only for post owner or super user

    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            request.user.is_authenticated()
        if request.method in ['PUT', 'DELETE']:
            return obj.user == request.user or request.user.is_superuser



