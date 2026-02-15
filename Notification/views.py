from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.reg_id
        queryset = Notification.objects.filter(receiver_id=user_id).order_by('-created_at')

        priority = request.query_params.get('priority')
        unread = request.query_params.get('unread')

        if priority:
            queryset = queryset.filter(priority__iexact=priority)
        if unread == 'true':
            queryset = queryset.filter(is_seen=False)

        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotificationDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, noti_id):
        try:
            notification = Notification.objects.get(noti_id=noti_id)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)

        if notification.receiver_id != request.user.reg_id:
            return Response({"error": "Action Not Allowed!"}, status=status.HTTP_403_FORBIDDEN)

        serializer = NotificationSerializer(notification)
        return Response(serializer.data)


class MarkAsSeenAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, noti_id):
        try:
            notification = Notification.objects.get(noti_id=noti_id)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)

        if notification.receiver_id != request.user.reg_id:
            return Response({"error": "Action Not Allowed!"}, status=status.HTTP_403_FORBIDDEN)

        notification.mark_read()
        return Response({"message": "Notification Marked As Seen!"}, status=status.HTTP_200_OK)
