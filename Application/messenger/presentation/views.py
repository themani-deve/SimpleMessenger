from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from core.base_view import BaseGenericView
from messenger.docs import CreatePrivateConversationViewDoc, ConversationListViewDoc, ConversationDetailViewDoc
from messenger.models import Conversation, Message
from messenger.services.conversation import PrivateConversationService
from .serializers.input import CreatePrivateConversationSerializer
from .serializers.output import ConversationDataSerializer, ConversationDetailDataSerializer


@CreatePrivateConversationViewDoc
class CreatePrivateConversationView(BaseGenericView):
    serializer_class = CreatePrivateConversationSerializer
    service_class = PrivateConversationService

    def post(self, request, *args, **kwargs):
        validated_data = self.get_validated_data()

        data = self.get_service().create_private_conversation(user_id=request.user.id, **validated_data)
        response = ConversationDataSerializer(data, context={"request": request}).data

        return Response(data=response, status=status.HTTP_201_CREATED)


@ConversationListViewDoc
class ConversationListView(generics.ListAPIView):
    serializer_class = ConversationDataSerializer

    def get_queryset(self):
        return Conversation.objects.filter(members__user=self.request.user).distinct()


@ConversationDetailViewDoc
class ConversationDetailView(generics.ListAPIView):
    serializer_class = ConversationDetailDataSerializer

    def get_queryset(self):
        conversation_id = self.kwargs["conversation_id"]
        conversation = Conversation.objects.filter(id=conversation_id, members__user=self.request.user).exists()

        if not conversation:
            raise PermissionDenied("You do not have access to this conversation.")

        return Message.objects.filter(conversation_id=conversation_id).distinct()
