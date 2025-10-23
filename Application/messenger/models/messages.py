from django.db import models

from core.base_model import BaseModel
from .conversation import Conversation
from .conversation_members import ConversationMember


class Message(BaseModel):
    class Meta:
        db_table = "messages"
        ordering = ["-created_at"]

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    conversation_member = models.ForeignKey(ConversationMember, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"{self.conversation} --- {self.conversation_member}"
