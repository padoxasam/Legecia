from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SupervisedPack
from .serializers import SupervisedPackSerializer
from .permissions import IsUserCreator,IsGuardian,IsBeneficiaryView
from django.shortcuts import get_object_or_404

class CreateSupervision(APIView):
    permission_classes=[IsAuthenticated,IsUserCreator]
    def post(self,request):
        
        serializer=SupervisedPackSerializer(data=request.data ,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save(supervision_status='Draft')
        return Response({'message': 'Supervised Package Created As draft !','data':serializer.data})
class SendSupervisionRequest(APIView):
    permission_classes=[IsAuthenticated,IsUserCreator]
    def post(self,request,supervision_id):
        obj=get_object_or_404(SupervisedPack,pk=supervision_id,user=request.user)
        if obj.supervision_status !='Draft':
            return Response({'error': 'Only draft packages can be sent'}, status=400)
        obj.supervision_status='Pending'
        obj.save(update_fields=['supervision_status'])
        serializer=SupervisedPackSerializer(obj)
        return Response ({'message': 'Supervision request sent to guardian',
            'data': serializer.data})
class BeneficiaryViewSupevision(APIView):
    permission_classes=[IsAuthenticated,IsBeneficiaryView]
    def get (self,request,superivision_id):
        object=get_object_or_404(SupervisedPack,pk=superivision_id)
        if object.beneficairy_id !=request.user.id:
            return Response({'Error': 'Action Prohibited!'},status=403)
        serializer=SupervisedPackSerializer(object)
        return Response(serializer.data)

