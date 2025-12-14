from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .serializers import NotificationSerializer
from .permissions import IsNotificationOwner

class NotificationListAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user_id=request.user.id
        queryset = Notification.objects.filter(receiver_object_id=user_id).order_by('-created_at')
        priority=request.query_params.get('priority')
        unread=request.query_params.get('unread')
        noti_type=request.query_params.get('type')
        if priority:
            queryset=queryset.filter(priority=priority.upper())
        if unread == 'True':
            queryset = queryset.filter(is_seen=False)

        if noti_type:
            queryset=queryset.filter(notification_type=noti_type)
        serializer=NotificationSerializer(queryset,many=True)
        return Response(serializer.data,status=200)
class NotificationDetailAPI(APIView):
    permission_classes=[IsAuthenticated,IsNotificationOwner]
    def get_receiver_type(self, obj):
        if obj.receiver_content_type:
            return obj.receiver_content_type.model_class().__name__
        return None

        

class MarkAsSeenAPI(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,noti_id):
        try:
            notification=Notification.objects.get(noti_id=noti_id)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found"}, status=404)
        if notification.receiver_id !=request.user.id:
            return Response({'Error':'Action Not Allowed !'},status=403)
        notification.is_seen=True
        notification.save()
        return Response ({'Messsage':'Notification Marked As Seen !'},status=200)
