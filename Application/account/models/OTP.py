from django.db import models
from django.utils import timezone

from core.base_model import BaseModel
from .user import User


class OTP(BaseModel):
    class Meta:
        db_table = "otp"
        ordering = ["-created_at"]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.code}"

    def is_expired(self):
        return self.expired_at < timezone.now()
