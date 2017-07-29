from rest_framework.permissions import BasePermission
from .models import KeystoneData


class IsOwner(BasePermission):
    """Custom permission class to allow only keystonedata owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the keystonedata owner."""
        if isinstance(obj, KeystoneData):
            return obj.owner == request.user
        return obj.owner == request.user