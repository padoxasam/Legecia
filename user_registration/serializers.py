from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
import re

User = get_user_model()


# =========================
# REGISTER SERIALIZER
# =========================
class RegisterSerializer(serializers.ModelSerializer):
    # 🔁 Map frontend → model
    username = serializers.CharField(source="u_username")
    email = serializers.EmailField(source="u_email")

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
    def validate_u_email(self, value):
        if User.objects.filter(u_email__iexact=value).exists():
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
            raise serializers.ValidationError(
                {"password2": "Passwords do not match"}
            )
        return attrs

    # ---------- CREATE USER ----------
    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")

        user = User.objects.create_user(
            u_username=validated_data["u_username"],
            u_email=validated_data["u_email"],
            password=password,
            active_role="USER",
        )

        return user


# =========================
# LOGIN SERIALIZER
# =========================
class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)  # username OR email
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        login = data.get("login")
        password = data.get("password")

        if not login or not password:
            raise serializers.ValidationError("Both fields are required")

        # 🔁 Email OR username login
        if "@" in login:
            try:
                user_obj = User.objects.get(u_email__iexact=login)
                login = user_obj.u_username
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid credentials")

        user = authenticate(username=login, password=password)
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
class UpdateProfileSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def validate_email(self, value):
        user = self.instance
        if (
            User.objects
            .filter(u_email__iexact=value)
            .exclude(reg_id=user.reg_id)
            .exists()
        ):
            raise serializers.ValidationError("Email already in use")
        return value

    def update(self, instance, validated_data):
        email = validated_data.get("email")
        username = validated_data.get("username")

        if email and email != instance.u_email:
            instance.email_verified = False
            instance.u_email = email

        if username:
            instance.u_username = username

        instance.save()
        return instance
