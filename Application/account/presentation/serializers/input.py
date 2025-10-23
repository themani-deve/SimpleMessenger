from rest_framework import serializers

from account.models import User


class SentOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=11, max_length=11)


class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=11, max_length=11)
    otp_code = serializers.CharField(min_length=6, max_length=6)


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "profile_image"]
