from rest_framework import serializers
import re




class ProfileSerializer(serializers.Serializer):
    full_name=serializers.CharField(required=True , max_length=200)

    gender_choices=(('male','MALE'),
                    ('female','FEMALE'),) #  candian in big-trouble
    
    phone_num=serializers.CharField(required=True)
    gender=serializers.ChoiceField(choices=gender_choices )
    dob=serializers.DateField(required=False)
    family_title=serializers.CharField(required=False,max_length=100)
    address=serializers.CharField(required=False)
    bio=serializers.CharField(required=False,allow_blank=True)

    def validate_phone(self,value):
        if not value:
            return value 
        if not re.fullmatch(r'\d{8,11}',value):
            raise serializers.ValidationError('Phone Number must contain digits and only 8-11 characters long ! ')
        return value