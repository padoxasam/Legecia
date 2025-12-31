
# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Package
from .serializers import PackageSeriializer
class PackageListCreateView(generics.ListCreateAPIView):
    queryset=Package.objects.all()
    serializer_class=PackageSeriializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        querys=super().get_queryset()
        owner_id=self.request.query_params.get('owner')
        if owner_id:
            querys=querys.filter(owner_id=owner_id)
        return querys
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)

class PackageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PackageSeriializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Package.objects.all()
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])

    
    
    def update(self, request, *args, **kwargs):
        package = self.get_object()

        if package.owner_id != request.user.id and not request.user.is_staff:
            return Response(
                {"detail": "Not allowed"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        package = self.get_object()
        if package.owner_id != request.user.id and not request.user.is_staff:
            return Response(
                {"detail": "Not allowed"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(request, *args, **kwargs)