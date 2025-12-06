from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .serializers import MilestoneSerializer
from .models import Milestone
from .permissions import IsUser,IsBene

class UserCreateMilestone(APIView):
    permission_classes=[IsAuthenticated,IsUser]

    def post(self,request):
        serializer=MilestoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, beneficiary=None)
            return Response(serializer.errors,status=400)
class BeneficiaryUploadMilestone(APIView):
    permission_classes=[IsAuthenticated,IsBene]


    def post(self,request,milestone_id):
        try:
            milestone=Milestone.objects.get(milestone_id=milestone_id)
        except Milestone.DoesNotExist:
            return Response({'ERROR':'Milestone Not Found !'},status=404)
        serializer=MilestoneSerializer(milestone,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(beneficiary=request.user.beneficiary)
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
class MilestoneDetails(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,milestone_id):
        try:
            milestone=Milestone.objects.get(milestone_id=milestone_id)
        except Milestone.DoesNotExist:
            return Response({'Error':'Not Found !'},status=404)
        serializer=MilestoneSerializer(milestone)
        return Response(serializer.data)