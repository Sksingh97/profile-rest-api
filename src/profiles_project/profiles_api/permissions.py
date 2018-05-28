from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow User To Update There Own Status"""

    def has_object_permission(self, request, view, obj):
        """Check The User Trying To Update Theire Own Status."""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
