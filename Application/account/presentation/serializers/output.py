from rest_framework import serializers
from rest_framework.reverse import reverse

from account.models import User
from core.base_serializer import BaseDataSerializer


# ========== Start token serializer ==========

class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class TokenDataSerializer(serializers.Serializer):
    tokens = TokenSerializer()


# ========== End token serializer ==========


# ========== Start profile serializer ==========


class ProfileLinkSerializer(serializers.Serializer):
    self = serializers.HyperlinkedIdentityField(view_name="user-profile", lookup_field="pk")
    profile_image = serializers.SerializerMethodField()
    conversation = serializers.SerializerMethodField()

    def get_profile_image(self, obj):
        request = self.context.get('request')
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)
        return None

    def get_conversation(self, obj):
        return reverse(viewname="new-private-conversation", request=self.context.get("request"))


class ProfileAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "phone_number", "username"]


class ProfileDataSerializer(BaseDataSerializer):
    links = ProfileLinkSerializer(source="*")
    attributes = ProfileAttributeSerializer(source="*")

# ========== End profile serializer ==========
