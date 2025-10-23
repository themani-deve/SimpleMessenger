from uuid import UUID

from account.services.helper import UserHelper
from messenger.models import Conversation
from .conversation_member import ConversationMemberService


class BaseConversation:
    """
    All services related to creating a conversation should inherit from this class as the 'base' class.
    """

    def __init__(self, conversation_model: type[Conversation] = Conversation):
        self.conversation_model = conversation_model

    def _create_conversation(self, conversation_type: str, title: str) -> Conversation:
        """
        This method is used to create a new conversation.
        """
        return self.conversation_model.objects.create(conversation_type=conversation_type, title=title)


class PrivateConversationService(BaseConversation):
    def __init__(
            self,
            conversation_model: type[Conversation] = Conversation,
            user_helper: type[UserHelper] = UserHelper,
            conversation_member_service: type[ConversationMemberService] = ConversationMemberService,
    ):
        super().__init__(conversation_model=conversation_model)
        self.user_helper = user_helper
        self.conversation_member_service = conversation_member_service

    def create_private_conversation(self, user_id: UUID, other_user_id: UUID, title: str = None) -> Conversation:
        """
        This method is responsible for creating a 'private' conversation.
        """
        user_helper = self.user_helper()

        # If user not found -> raise UserNotFoundError()
        user_helper.get_user(id=user_id)
        user_helper.get_user(id=other_user_id)

        conversation = self._find_conversation(user_id=user_id, other_user_id=other_user_id)

        if not conversation:
            conversation = self._create_conversation(conversation_type="private", title=title)
            conversation_member_service = self.conversation_member_service()

            for uid in [user_id, other_user_id]:
                conversation_member_service.create_member(conversation_id=conversation.id, user_id=uid)

        return conversation

    def _find_conversation(self, user_id: UUID, other_user_id: UUID) -> Conversation | None:
        """
        This method is responsible for checking if a 'private' conversation exists between two users requesting
        to create a conversation.
        This method is added solely to increase readability and reduce the number of lines of code in the main method.
        """
        return (
            self.conversation_model.objects.filter(conversation_type="private")
            .filter(members__user_id=user_id)
            .filter(members__user_id=other_user_id)
            .first()
        )
