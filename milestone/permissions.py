from rest_framework.permissions import BasePermission

class IsBene(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user,'account_type') and request.user.account_type=='USER'
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user,'account_type') and request.user.account_type=='BENEFICIARY'
    