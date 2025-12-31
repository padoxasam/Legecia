from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
import re

User = get_user_model()


# =========================
# REGISTER SERIALIZER
# =========================
class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # ---------- EMAIL VALIDATION ----------
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Invalid email address format")

        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already registered")

        return value

    # ---------- PASSWORD VALIDATION ----------
    def validate_password1(self, value):
        return self._validate_password(value)

    def validate_password2(self, value):
        return self._validate_password(value)

    def _validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long"
            )
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter"
            )
        if not re.search(r"\d", value):
            raise serializers.ValidationError(
                "Password must contain at least one digit"
            )
        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", value):
            raise serializers.ValidationError(
                "Password must contain at least one special character"
            )
        return value

    # ---------- MATCH PASSWORDS ----------
    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError({
                "password2": "Passwords do not match"
            })
        return attrs

    # ---------- CREATE USER ----------
    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")

        user = User.objects.create_user(**validated_data)
        user.set_password(password)

        user.active_role = "USER"
        user.email_verified = False
        user.save()

        return user


# =========================
# LOGIN SERIALIZER
# =========================
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise serializers.ValidationError("Both fields are required")

        # Allow login with email or username
        if "@" in username:
            try:
                user_obj = User.objects.get(email__iexact=username)
                username = user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid credentials")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data


# =========================
# ROLE SWITCH SERIALIZER
# =========================
class RoleSwitchSerializer(serializers.Serializer):
    role = serializers.ChoiceField(
        choices=["USER", "BENEFICIARY", "GUARDIAN"]
    )


# =========================
# UPDATE PROFILE SERIALIZER
# =========================
class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email"]

    def validate_email(self, value):
        user = self.instance
        if (
            User.objects
            .filter(email__iexact=value)
            .exclude(id=user.id)
            .exists()
        ):
            raise serializers.ValidationError("Email already in use")
        return value

    def update(self, instance, validated_data):
        email = validated_data.get("email")

        # Reset email verification if email changes
        if email and email != instance.email:
            instance.email_verified = False
            instance.email = email

        instance.username = validated_data.get(
            "username", instance.username
        )

        instance.save()
        return instance
