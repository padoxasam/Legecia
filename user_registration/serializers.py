import serlializers from rest_framework
import validate_password from django.contrib.auth.password_validation
import user from .models

class Registerserializer(serlializers.Modelserilizer):

    n_password=serlializers.CharField(write_only=True , required=True, validators=[validate_password])
    re_password=serlializers.CharField(write_only=True , required=True, validators=[validate_password])

    class meta:
        model=User 
        fields = ( 'username', 'e-mail','n_password','re_password')

        def validate (self , attr):
            if attr['n_passwprd'] != attr['re_password']:
                raise serlializers.ValidationError(['password', 'Passwords do not match !']) 
            return attr

        def create (self, validated_data):
            validated_data.pop('re_password') 
            user=User.object.create_user(**validated_data)
            return user   