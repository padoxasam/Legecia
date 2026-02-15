from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import PackageExplorer
from .serializers import PackExplorerSerializer
from .permissions import CanViewPublicPackages, IsOwnerListing


class PublicPackageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = PackageExplorer.objects.filter(is_public=True)
        serializer = PackExplorerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PublicPackageCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data["ownership"] = request.user.reg_id

        serializer = PackExplorerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicPackageDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerListing]

    def get_object(self, pk):
        obj = get_object_or_404(PackageExplorer, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = PackExplorerSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({"detail": "Listing removed."}, status=status.HTTP_204_NO_CONTENT)
