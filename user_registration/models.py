from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, u_username, u_email, password=None, **extra_fields):
        if not u_username:
            raise ValueError("Username is required")
        if not u_email:
            raise ValueError("Email is required")
        user = self.model(
            u_username=u_username,
            u_email=self.normalize_email(u_email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, u_username, u_email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(u_username, u_email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    reg_id = models.AutoField(primary_key=True)
    u_username = models.CharField(max_length=150, unique=True)
    u_email = models.EmailField(unique=True)
    u_full_name = models.CharField(max_length=255)
    
    email_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # 📱 DEVICE & TOKEN FIELDS
    qr_token = models.CharField(max_length=512, blank=True, null=True)
    device_verified = models.BooleanField(default=False)
    
    active_role = models.CharField(
        max_length=20,
        default="USER",
        choices=[
            ("USER", "User"),
            ("BENEFICIARY", "Beneficiary"),
            ("GUARDIAN", "Guardian"),
        ],
    )
    
    # ⏱ META FIELDS
    last_seen = models.DateTimeField(null=True, blank=True)
    u_creation_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "u_username"
    REQUIRED_FIELDS = ["u_email"]

    class Meta:
        db_table = "legecia.user_registration"
        managed = False  # 🔥 CRITICAL

    def __str__(self):
        return self.u_username


class Beneficiary(models.Model):
    b_id = models.AutoField(primary_key=True)
    
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="beneficiary_profile"
    )
    
    b_full_name = models.CharField(max_length=255, null=True, blank=True)
    b_username = models.CharField(max_length=255)
    b_email = models.EmailField(null=True, blank=True)
    b_u_relation = models.CharField(max_length=50, null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = "beneficiary"
        managed = False

    def __str__(self):
        return self.b_username


class Guardian(models.Model):
    g_id = models.AutoField(primary_key=True)
    
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="guardian_profile"
    )
    
    g_full_name = models.CharField(max_length=255, null=True, blank=True)
    g_username = models.CharField(max_length=255)
    g_email = models.EmailField(null=True, blank=True)
    relation_u = models.CharField(max_length=50, null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = "legecia.guardian_info"
        managed = False

    def __str__(self):
        return self.g_username