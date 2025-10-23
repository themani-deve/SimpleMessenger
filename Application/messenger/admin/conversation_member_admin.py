from django.contrib import admin

from messenger.models import ConversationMember


@admin.register(ConversationMember)
class ConversationMemberAdmin(admin.ModelAdmin):
    list_display = ["conversation", "user"]

    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    fieldsets = [
        ["Basic information", {"fields": ["id", "conversation", "user"]}],
        ["Conversation member information", {"fields": ["created_at", "updated_at"]}],
    ]

    readonly_fields = ["id", "created_at", "updated_at"]
