from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Beneficiary
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
import re 
from django.db import connection

account_type_tuple=[
    ('USER','User'),
             ('BENEFICIARY','Beneficiary'),
             ('GUARDIAN','Guardian'),

]
User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):

    n_password=serializers.CharField(write_only=True , required=True, validators=[validate_password],style={'input_type': 'password'})
    r_password=serializers.CharField(write_only=True , required=True, validators=[validate_password],style={'input_type': 'password'})
    account_type= serializers.ChoiceField(choices=account_type_tuple, write_only=True,required=True,allow_null=False,allow_blank=False)

    class Meta:
        model=User 
        fields = ( 'username', 'email','n_password','r_password','account_type',)
        resetting={'account_type':{'default':None}}
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email Already Registered')

    def validate_account_type(self, val):
        if val not in ["USER", "BENEFICIARY", "GUARDIAN"]:
            raise serializers.ValidationError("Invalid account type")
        return val

    def validate_email2(self,id):
        if '@' not in id:
            raise serializers.ValidationError('Invalid E-mail Address ❌')
        return id
    def password_Validation (self , attr):
        if attr['n_password'] != attr['r_password']:
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
    
    def create(self, validated_data):
        validated_data.pop('r_password')
        password = validated_data.pop('n_password')
        account_type = validated_data.pop('account_type')

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        if account_type == "USER":
            with connection.cursor() as cursor:
                cursor.execute(
                """
                INSERT INTO user_info (u_full_name, u_username, u_email)
                VALUES (%s, %s, %s)
                """,
                [user.full_name, user.username, user.email])

        elif account_type == "BENEFICIARY":
            Beneficiary.objects.create(
                    b_full_name=user.full_name,
                    b_email=user.email,
                    b_username=user.username)

        elif account_type == "GUARDIAN":
            from .models import Guardian # ab3a 7tha fo3 
            Guardian.objects.create(
            g_full_name=user.full_name,
            g_email=user.email,
            g_username=user.username,)

        return user
class LoginSerializer(serializers.Serializer):
    identifier=serializers.CharField(required=True)
    password=serializers.CharField(required=True,write_only=True)

    def validate(self,data):
        identifier=data.get('identifier')
        password=data.get('password')
        if not identifier or not password:
            raise serializers.ValidationError('Both Fields are Required')
        if '@'in identifier:
            try:
                user_obj=User.objects.get(email__iexact=identifier)
                username=user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid Credentials !')
        else:
            username=identifier
        user=authenticate(username=username,password=password)
        if not user:
            raise serializers.ValidationError('Invalid Credentials !')
        data['user']=user
        return data