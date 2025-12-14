from rest_framework import serializers
import re
from django_countries.serializer_fields import CountryField


class ProfileSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=True, max_length=200)

    gender_choices = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )

    phone_num = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=gender_choices)
    dob = serializers.DateField(required=False)
    family_title = serializers.CharField(required=False, max_length=100)
    address = serializers.CharField(required=False)
    bio = serializers.CharField(required=False, allow_blank=True)
    nationality = CountryField(required=False)
    region = serializers.IntegerField(required=False)

    active_role = serializers.ChoiceField(
        choices=('USER', 'BENEFICIARY', 'GUARDIAN'),
        write_only=True
    )

    relation_choices = (
        ('MOTHER', 'MOTHER'),
        ('FATHER', 'FATHER'),
        ('GRANDMOTHER', 'GRANDMOTHER'),
        ('GRANDFATHER', 'GRANDFATHER'),
        ('BROTHER', 'BROTHER'),
        ('SISTER', 'SISTER'),
        ('UNCLE', 'UNCLE'),
        ('AUNT', 'AUNT'),
        ('COUSIN', 'COUSIN'),
        ('NIECE', 'NIECE'),
        ('NEPHEW', 'NEPHEW'),
        ('FAMILY_FRIEND', 'FAMILY FRIEND'),
        ('MENTOR', 'MENTOR'),
        ('SOCIAL_WORKER', 'SOCIAL WORKER'),
        ('LEGAL_GUARDIAN', 'LEGAL GUARDIAN'),
        ('FOSTER_PARENT', 'FOSTER PARENT'),
        ('CARETAKER', 'CARETAKER'),
        ('OTHER', 'OTHER'),
    )

    relation_to_user = serializers.ChoiceField(
        choices=relation_choices,
        required=False
    )

    def validate_phone_num(self, value):
        if not re.fullmatch(r'\d{8,11}', value):
            raise serializers.ValidationError(
                'Phone number must be 8–11 digits.'
            )
        return value

    def validate(self, data):
        role = data.get("active_role")

        if role in ("BENEFICIARY", "GUARDIAN") and not data.get("relation_to_user"):
            raise serializers.ValidationError({
                "relation_to_user": "Relation is required for this role."
            })

        return data
