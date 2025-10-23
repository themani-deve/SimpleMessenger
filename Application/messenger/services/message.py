from uuid import UUID

from messenger.models import Message


class MessageService:
    def __init__(self, message_model: type[Message] = Message):
        self.message_model = message_model

    def create_message(self, conversation_id: UUID, member_id: UUID, message: str) -> Message:
        """
        This method is used to create a message for a conversation.
        """
        return self.message_model.objects.create(
            conversation_id=conversation_id,
            conversation_member_id=member_id,
            message=message
        )
