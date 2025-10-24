from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):

    n_password=serializers.CharField(write_only=True , required=True, validators=[validate_password])
    re_password=serializers.CharField(write_only=True , required=True, validators=[validate_password])

    class Meta:
        model=User 
        fields = ( 'username', 'email','n_password','re_password')

        def validate (self , attr):
            if attr['n_password'] != attr['re_password']:
                raise serializers.ValidationError({'password', 'Passwords do not match !'}) 
            return attr

        def create (self, validated_data):
            validated_data.pop('re_password')
            password=validated_data.pop('n_password') 
            user=User.objects.create_user(**validated_data)
            user.set_password(password)
            user.save()
            return user   