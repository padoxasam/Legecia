from rest_framework import serializers
from .models import PackExplorer

class PackExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackExplorer
        fields = "__all__"
