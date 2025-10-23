from rest_framework import serializers
from rest_framework.reverse import reverse

from core.base_serializer import BaseDataSerializer
from messenger.models import Conversation, Message


# ========== Start conversation list serializer ==========


class ConversationLinkSerializer(serializers.Serializer):
    self = serializers.SerializerMethodField()

    def get_self(self, obj):
        request = self.context.get("request")
        return reverse("conversation-detail", kwargs={"conversation_id": obj.pk}, request=request)


class ConversationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "title", "conversation_type", "created_at", "updated_at"]


class ConversationDataSerializer(BaseDataSerializer):
    links = ConversationLinkSerializer(source="*")
    attributes = ConversationAttributeSerializer(source="*")


# ========== End conversation list serializer ==========

# ========== Start conversation detail serializer ==========


class ConversationDetailLinkSerializer(serializers.Serializer):
    conversation = serializers.SerializerMethodField()
    conversation_member = serializers.SerializerMethodField()

    def get_conversation(self, obj):
        request = self.context.get("request")
        return reverse("conversation-detail", kwargs={"conversation_id": obj.conversation.pk}, request=request)

    def get_conversation_member(self, obj):
        request = self.context.get("request")
        return reverse(viewname="user-profile", kwargs={"pk": obj.conversation_member.user.id}, request=request)


class ConversationDetailAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "message", "created_at", "updated_at"]


class ConversationDetailDataSerializer(BaseDataSerializer):
    links = ConversationDetailLinkSerializer(source="*")
    attributes = ConversationDetailAttributeSerializer(source="*")

# ========== End conversation detail serializer ==========
