from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "is_active", "is_staff", "is_superuser"]

    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["first_name", "last_name", "username", "phone_number"]
    ordering = ["-created_at"]

    list_editable = ["is_active"]

    fieldsets = [
        ["Basic information", {"fields": ["id", "first_name", "last_name", "username", "phone_number"]}],
        [
            "Account information",
            {
                "fields": ["profile_image", "is_active", "is_staff", "is_superuser", "created_at", "updated_at"]
            }
        ],
    ]

    readonly_fields = ["id", "created_at", "updated_at"]
