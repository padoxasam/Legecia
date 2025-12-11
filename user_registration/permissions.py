from rest_framework.permissions import BasePermission

class IsUserRole(BasePermission):

    def has_permission(self, request, view):
        return request.user.active_role == 'USER'
class IsBeneficiaryRole(BasePermission):

    def has_permission(self, request, view):
        return request.user.active_role == 'BENEFICIARY'
class IsGuardianRole(BasePermission):

    def has_permission(self, request, view):
        return request.user.active_role == 'GUARDIAN'