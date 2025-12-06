from rest_framework import serializers
from .models import PackageExplorer

class PackExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageExplorer
        fields = "__all__"
