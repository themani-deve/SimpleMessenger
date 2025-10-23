from django.db import models

from core.base_model import BaseModel


class ConversationTypeChoices(models.TextChoices):
    private = "private", "private"
    group = "group", "group"


class Conversation(BaseModel):
    class Meta:
        db_table = "conversations"
        ordering = ["-created_at"]

    conversation_type = models.CharField(max_length=255, choices=ConversationTypeChoices)
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.conversation_type} --- {self.title}"
