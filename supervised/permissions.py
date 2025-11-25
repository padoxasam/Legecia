from rest_framework.permissions import BasePermission

class IsUserCreator (BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type=='USER'
class IsGuardian(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.account_type=='Guardian'
class IsBeneficiaryView(BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type=='BENEFICIARY'