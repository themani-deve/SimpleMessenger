from django.contrib import admin
from messenger.models import Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["conversation_type", "title"]

    list_filter = ["conversation_type", "created_at", "updated_at"]
    search_fields = ["title"]
    ordering = ["-created_at"]

    fieldsets = [
        ["Basic information", {"fields": ["id", "conversation_type", "title"]}],
        ["Conversation information", {"fields": ["created_at", "updated_at"]}],
    ]

    readonly_fields = ["id", "created_at", "updated_at"]
