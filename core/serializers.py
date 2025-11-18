from rest_framework import serializers
import re
from django_countries.serializer_fields import CountryField



class ProfileSerializer(serializers.Serializer):
    full_name=serializers.CharField(required=True , max_length=200)

    gender_choices=(('MALE','MALE'),
                    ('FEMALE','FEMALE'),) #  candian in big-trouble
    
    phone_num=serializers.CharField(required=True)
    gender=serializers.ChoiceField(choices=gender_choices )
    dob=serializers.DateField(required=False)
    family_title=serializers.CharField(required=False,max_length=100)
    address=serializers.CharField(required=False)
    bio=serializers.CharField(required=False,allow_blank=True)
    nationality=CountryField(required=False)
    region=serializers.IntegerField(required=False)
    relation_choices= ( # kl elentities 
                        ('MOTHER','MOTHER'),
                       ('FATHER','FATHER'),
                       ('GRANDMOTHER','GRANDMOTHER'),
                       ('GRANDFATHER','GRANDFATHER'),
                       ('STEP FATHER','STEP FATHER'),
                       ('STEP MOTHER','STEP MOTHER'),
                       ('BROTHER','BROTHER'),
                       ('SISTER','SISTER'),
                       ('UNCLE','UNCLE'),
                       ('AUNT','AUNT'),
                       ('COUNSIN','COUNSIN'),
                       ('NEPTHEW','NEPTHEW'),
                       ('NIECE','NIECE'),
                       ('FAMILY FRIEND','FAMILY FRIEND'),
                       ('NEIGHBOR','NEIGHBOR'),
                       ('MENTOR','MENTOR'),
                       ('SOCIAL WORKER','SOCIAL WORKER'),
                       ('OTHER','OTHER'),
                       # -- -- Guardian exc -- - - -- 
                        ('LEGEAL_GUARDIAN','LEGEAL_GUARDIAN'),
                        ('FOSTER PARENT','FOSTER PARENT'),
                        ('CARETAKER','CARETAKER'),

    )

    beneficiary_user_relation=serializers.ChoiceField(choices=relation_choices,required=False)
    guardian_user_relation=serializers.ChoiceField(choices=relation_choices,required=False)
    guardian_beneficiary_relation=serializers.ChoiceField(choices=relation_choices,required=False)

    def validate_phone_num(self,value):
        if not value:
            return value 
        if not re.fullmatch(r'\d{8,11}',value):
            raise serializers.ValidationError('Phone Number must contain digits and only 8-11 characters long ! ')
        return value