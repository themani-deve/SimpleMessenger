from rest_framework import serializers

from messenger.models import Conversation


class CreatePrivateConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["title", "other_user_id"]

    other_user_id = serializers.UUIDField()
