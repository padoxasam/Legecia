from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SupervisedPack
from .serializers import SupervisedPackSerializer
from .permissions import IsUserCreator,IsGuardian,IsBeneficiaryView

class CreateSupervision(APIView):
    permission_classes=[IsAuthenticated,IsUserCreator]
    def post(self,request):
        serializer=SupervisedPackSerializer(data=request.data,context={'Request':request})
        serializer.save()
        return Response({'Message':'Package Supervision'  , "DATA":serializer.data})
class GuardianUpdateSupervision(APIView):
    permission_classes=[IsAuthenticated,IsGuardian]
    def put(self,request,supervision_id):
        try:
            obj=SupervisedPack.objects.get(pk=supervision_id)
        except SupervisedPack.DoesNotExist:
            return Response({'Error':'Supervision Not Found !'},status=404)
        serializer=SupervisedPackSerializer(obj,data=request.data,partial=True,context={'Request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Message':'Guardian Updated Supervision !','data':serializer.data})
class BeneficiaryViewSupevision(APIView):
    permission_classes=[IsAuthenticated,IsBeneficiaryView]
    def get (self,request,superivision_id):
        try:
            object=SupervisedPack.objects.get(pk=superivision_id)
        except SupervisedPack.DoesNotExist:
            return response({'Error':'Supervision Not Found !'},status=404)
        if object.ben.reg_id !=request.user.reg_id:
            return Response({'Error': 'Action Prohibited !'},status=403)
        serializer=SupervisedPackSerializer(object)
        return Response(serializer.data
                        )