from rest_framework.permissions import BasePermission

class IsUserCreator (BasePermission):
    def has_permission(self, request, view):
             return request.user.is_authenticated and request.user.active_role == 'USER'
            
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.active_role == 'GUARDIAN' and obj.guardian_id == request.user.id

class IsBeneficiaryView(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.active_role == 'BENEFICIARY'