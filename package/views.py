from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Package
from .serializer import PackageSerializer
class PackageListCreateView(generics.ListCreateAPIView):
    queryset=Package.objects.all()
    serializer_class=PackageSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        querys=super().get_queryset()
        owner_id=self.request.query_params.get('owner')
        if owner_id:
            querys=querys.filter(owner_id=owner_id)
        return querys
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class PackageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Package.objects.all()
    serializer_class=PackageSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        object=get_object_or_404(Package,pk=self.kwargs.get('pk'))
        return object
    def put(self,request,*args,**kwargs):
        object=self.get_object()

        if object.owner != request.user and not request.user.is_staff:
            return response ({'details':'Not Allowed !'}, status=status.HTTP_403_FORBIDDEN
                             )
        return super().put(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        object=self.get_object ()
        if obj.owner !=request.user and not request.user.is_stuff:
            return Response({'Details': 'Not Allowed ! '}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request,*args, **kwargs)