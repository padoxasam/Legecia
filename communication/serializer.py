from rest_framework import serializers
from .models import CommunicationMeans
class CommunicationSerializer(serializers.ModelSerializer):
    class meta:
        model = CommunicationMeans
        fields='__all__'
        