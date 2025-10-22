from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from core.base_model import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, phone_number: str, password: str = None, **extra_fields):
        return self._create_user(phone_number=phone_number, password=password, **extra_fields)

    def create_superuser(self, phone_number: str, password: str = None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self._create_user(phone_number=phone_number, password=password, **extra_fields)

    def _create_user(self, phone_number: str, password: str = None, **extra_fields):
        if not phone_number:
            raise ValueError("phone_number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    phone_number = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=128, unique=True, null=True, blank=True)

    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    objects = UserManager()

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
