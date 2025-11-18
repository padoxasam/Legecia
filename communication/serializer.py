from rest_framework import serializers
from .models import communicationMeans
class CommunicationSerializer(serializers.ModelSerializer):
    class meta:
        model = communicationMeans
        fields='__all__'
        