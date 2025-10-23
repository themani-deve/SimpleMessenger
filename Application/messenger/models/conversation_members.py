from django.db import models

from account.models import User
from core.base_model import BaseModel
from .conversation import Conversation


class ConversationMember(BaseModel):
    class Meta:
        db_table = "conversation_members"
        ordering = ["-created_at"]
        unique_together = ["conversation", "user"]

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.conversation} --- {self.user}"
