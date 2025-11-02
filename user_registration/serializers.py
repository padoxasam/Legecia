from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

import re 

User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):

    n_password=serializers.CharField(write_only=True , required=True, validators=[validate_password])
    r_password=serializers.CharField(write_only=True , required=True, validators=[validate_password])

    class Meta:
        model=User 
        fields = ( 'username', 'email','n_password','re_password')
        def user_exist(self,value):
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError('Email Already Registered')


        def email_validation(self,id):
            if '@' not in id:
                raise serializers.ValidationError('Invalid E-mail Address ❌')
            return id
        def password_Validation (self , attr):
            if attr['n_password'] != attr['re_password']:
                raise serializers.ValidationError({'password', 'Passwords do not match !'}) 
            return attr
        def password_policy (self, val):
            if len(val) < 8 :
                raise serializers.ValidationError('Password Must be Greater Than 8 Characters !')    
            if not re.search(r'[A-Z]', val):
                raise serializers.ValidationError('Password Must Contain at least one Upper-Case Letter [A-Z]')
            if not re.search(r'\d',val):
                raise serializers.ValidationError('Password Must Contain at Least One digit (0-9) ')
            if not re.search(r"[!@#$%^&*_+-?></(\)'\"]",val):
                raise serializers.ValidationError('Password Must contain at least one special Character [e.g:!@#$%^&*]')
            return val
        
        def create (self, validated_data):
            validated_data.pop('re_password')
            password=validated_data.pop('n_password') 
            user=User.objects.create_user(**validated_data)
            user.set_password(password)
            user.save()
            return user   