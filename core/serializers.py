from rest_framework import serializers
from .models import CoreProfile

class CoreProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreProfile
        fields = '__all__'
        read_only_fields = ['user']
