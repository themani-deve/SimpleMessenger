from rest_framework import serializers


class SentOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=11, max_length=11)


class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=11, max_length=11)
    otp_code = serializers.CharField(min_length=6, max_length=6)
