from rest_framework import serializers

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


class ProfileAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "phone_number", "username"]
        read_only_fields = ["id", "phone_number"]


class ProfileDataSerializer(BaseDataSerializer):
    links = ProfileLinkSerializer(source="*")
    attributes = ProfileAttributeSerializer(source="*")

# ========== End profile serializer ==========
