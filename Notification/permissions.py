from rest_framework.permissions import BasePermission

class IsNotificationOwner(BasePermission):
   
    def has_object_permission(self, request, view, obj):
        return obj.receiver_object_id == request.user.id
