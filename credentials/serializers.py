# credentials/serializers.py
from rest_framework import serializers
from .models import Credentials

class CredentialSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Credentials
        exclude = ("password_hashed", "password_salt")
    def validate(self, data):
        if len(data["password"]) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters.")
        return data
