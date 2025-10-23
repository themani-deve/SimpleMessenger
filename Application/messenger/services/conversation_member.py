from uuid import UUID

from messenger.models import ConversationMember


class ConversationMemberService:
    def __init__(self, conversation_member_model: type[ConversationMember] = ConversationMember):
        self.conversation_member_model = conversation_member_model

    def create_member(self, conversation_id: UUID, user_id: UUID) -> ConversationMember:
        """
        This method is responsible for creating a member for a conversation.
        """
        return self.conversation_member_model.objects.create(conversation_id=conversation_id, user_id=user_id)
