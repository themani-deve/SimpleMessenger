from rest_framework import serializers


class SentOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=11, max_length=11)


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=11, max_length=11)
    otp_code = serializers.CharField(min_length=6, max_length=6)
