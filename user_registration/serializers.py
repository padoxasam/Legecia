from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
import re 

account_type_tuple=[
    ('USER','User'),
             ('BENEFICIARY','Beneficiary'),
             ('GUARDIAN','Guardian'),]
User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):

    n_password=serializers.CharField(write_only=True , required=True, validators=[validate_password],style={'input_type': 'password'})
    r_password=serializers.CharField(write_only=True , required=True, validators=[validate_password],style={'input_type': 'password'})

    class Meta:
        model=User 
        fields = ( 'username', 'email','n_password','r_password')

    def validate_email(self, value):
        
        if '@' not in value:
            raise serializers.ValidationError('Invalid E-mail Address Format ❌')

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email Already Registered!')
        
        return value

    
    def validate_n_password(self, val):
        if len(val) < 8 :
            raise serializers.ValidationError('Password Must be Greater Than 8 Characters !')    
        if not re.search(r'[A-Z]', val):
            raise serializers.ValidationError('Password Must Contain at least one Upper-Case Letter [A-Z]')
        if not re.search(r'\d',val):
            raise serializers.ValidationError('Password Must Contain at Least One digit (0-9) ')
        if not re.search(r"[!@#$%^&*_+-?></(\)'\"]",val):
            raise serializers.ValidationError('Password Must contain at least one special Character [e.g:!@#$%^&*]')
        return val
    def validate(self , attr):
        if attr['n_password'] != attr['r_password']:
            raise serializers.ValidationError({'password', 'Passwords do not match !'}) 
        return attr
    def create(self, validated_data):
        validated_data.pop('r_password')
        password = validated_data.pop('n_password')

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.active_role='USER'
        user.save()
        return user

        
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True,write_only=True)

    def validate(self,data):
        username=data.get('username')
        password=data.get('password')
        if not username or not password:
            raise serializers.ValidationError('Both Fields are Required')
        if '@'in username:
            try:
                user_obj=User.objects.get(email__iexact=username)
                username=user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid Credentials !')
        else:
            username=username
        user=authenticate(username=username,password=password)
        if not user:
            raise serializers.ValidationError('Invalid Credentials !')
        data['user']=user
        return data
class RoleSwitchSerializer(serializers.Serializer):
    role=serializers.ChoiceField(choices=['USER','BENEFICIARY','GUARDIAN'])
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

    def validate_email(self, value):
        user = self.instance

        if User.objects.filter(email=value).exclude(id=user.id).exists():
            raise serializers.ValidationError("Email already in use")

        return value

    def update(self, instance, validated_data):
        email = validated_data.get('email')

        if email and email != instance.email:
            instance.email_verified = False

        instance.username = validated_data.get('username', instance.username)
        instance.email = email or instance.email
        instance.save()

        return instance