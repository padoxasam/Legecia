from rest_framework.permissions import BasePermission

class CanViewPublicPackages(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsOwnerListing(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.ownership == request.user
