from django.contrib import admin

from messenger.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["conversation", "conversation_member"]

    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    fieldsets = [
        ["Basic information", {"fields": ["id", "conversation", "conversation_member", "message"]}],
        ["Message information", {"fields": ["created_at", "updated_at"]}],
    ]

    readonly_fields = ["id", "created_at", "updated_at"]
