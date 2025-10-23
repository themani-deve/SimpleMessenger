import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from messenger.models import Conversation
from messenger.presentation.serializers.input import CreateMessageSerializer
from messenger.presentation.serializers.output import ConversationDetailDataSerializer
from messenger.services.message import MessageService


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, message_service: type[MessageService] = MessageService):
        super().__init__()
        self.message_service = message_service
        self.conversation = None
        self.conversation_member = None
        self.group_name = None

    async def connect(self):
        conversation_id = self.scope["url_route"]["kwargs"]["conversation_id"]
        user = self.scope["user"]

        self.conversation = await self.find_conversation(id=conversation_id)
        if not self.conversation:
            return await self.close()

        self.conversation_member = await database_sync_to_async(
            lambda: self.conversation.members.filter(user_id=user.id).first()
        )()
        if not self.conversation_member:
            return await self.close()

        self.group_name = f"chat_{conversation_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if self.group_name:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        try:
            data = json.loads(text_data)

            serializer = CreateMessageSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data

            message = await database_sync_to_async(self.message_service().create_message)(
                conversation_id=self.conversation.id,
                member_id=self.conversation_member.id,
                **validated_data
            )

            response_data = await self.serialize_message(message)

            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "chat_message",
                    "data": response_data,
                }
            )
        except Exception as e:
            await self.send(text_data=json.dumps({"error": str(e)}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event["data"]))

    @database_sync_to_async
    def find_conversation(self, **kwargs) -> Conversation:
        return Conversation.objects.filter(**kwargs).first()

    @database_sync_to_async
    def serialize_message(self, message):
        return ConversationDetailDataSerializer(message, context={"request": FakeRequest(self.scope)}).data


class FakeRequest:
    def __init__(self, scope):
        self.scope = scope
        self.user = scope.get("user")
        self.method = "GET"
        self.GET = {}
        self.POST = {}
        self.COOKIES = {}
        self.META = {k.decode(): v.decode() for k, v in scope.get("headers", [])}

    def build_absolute_uri(self, relative_url="/"):
        scheme = self.scope.get("scheme", "http")
        host = self.META.get("host", "localhost:8000")

        if scheme in ("ws", "wss"):
            scheme = "https" if scheme == "wss" else "http"

        return f"{scheme}://{host}{relative_url}"
