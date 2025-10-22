from django.contrib import admin

from account.models import OTP


@admin.register(OTP)
class OtpAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "code", "expired_at"]

    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    fieldsets = [
        ["Basic information", {"fields": ["id", "user", "code"]}],
        ["Otp information", {"fields": ["expired_at", "created_at", "updated_at"]}]
    ]

    readonly_fields = ["id", "expired_at", "created_at", "updated_at"]
