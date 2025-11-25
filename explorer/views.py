from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import PackageExplorer
from .serializers import PackExplorerSerializer
from .permissions import CanViewPublicPackages, IsOwnerListing
class PublicPackageListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(Self,request):
        queryset = PackExplorer.objects.filter(is_public=True)
        serializer = PackExplorerSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
class PublicPackageCreateView(APIView):
    permission_classes=[IsAuthenticated
                        ]
    def post(self, request):
        data = request.data.copy()
        data["ownership"] = request.user.id

        serializer = PackExplorerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
class PublicPackageDetailView(APIView):
    permission_classes=[IsAuthenticated,IsOwnerListing]
    def get_object(self, pk):
        return PackageExplorer.objects.get(pk=pk)
    def get(self, request, pk):
        obj = self.get_object(pk)
        self.check_object_permissions(request, obj)
        serializer = PackExplorerSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        self.check_object_permissions(request, obj)
        obj.delete()
        return Response({"detail": "Listing removed."}, status=204)