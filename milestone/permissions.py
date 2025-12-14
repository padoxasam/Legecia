from rest_framework.permissions import BasePermission

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.active_role=='USER'
class IsBene(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.active_role == 'BENEFICIARY'
