from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from account.docs import SentOtpViewDoc, LoginViewDoc, ProfileViewDoc, OtherUserProfileViewDoc, GetListUserViewDoc
from account.models import User
from account.services.authentication import AuthenticationService
from core.base_serializer import DetailResponseSerializer
from core.base_view import BaseGenericView
from .serializers.input import SentOTPSerializer, VerifyOTPSerializer, UpdateProfileSerializer
from .serializers.output import TokenDataSerializer, ProfileDataSerializer, ProfileAttributeSerializer


@SentOtpViewDoc
class SentOTPView(BaseGenericView):
    permission_classes = [AllowAny]
    serializer_class = SentOTPSerializer
    service_class = AuthenticationService

    def post(self, request: Request, *args, **kwargs):
        validated_data = self.get_validated_data()

        data = self.get_service().sent_otp(**validated_data)
        response = DetailResponseSerializer(data).data

        return Response(data=response, status=status.HTTP_200_OK)


@LoginViewDoc
class VerifyOTPView(BaseGenericView):
    permission_classes = [AllowAny]
    serializer_class = VerifyOTPSerializer
    service_class = AuthenticationService

    def post(self, request: Request, *args, **kwargs):
        validated_data = self.get_validated_data()

        tokens = self.get_service().verify_otp(**validated_data)
        response = TokenDataSerializer(tokens).data

        return Response(data=response, status=status.HTTP_200_OK)


@ProfileViewDoc
class ProfileView(generics.RetrieveUpdateAPIView):
    http_method_names = ["get", "patch"]

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateProfileSerializer
        return ProfileDataSerializer

    def get_object(self):
        return self.request.user

    def patch(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        response = ProfileDataSerializer(data, context={"request": request}).data

        return Response(data=response, status=status.HTTP_200_OK)


@GetListUserViewDoc
class GetListUserView(generics.ListAPIView):
    serializer_class = ProfileDataSerializer
    queryset = User.objects.all()
    filterset_fields = ["phone_number", "username"]


@OtherUserProfileViewDoc
class OtherUserProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileDataSerializer
    queryset = User.objects.all()
    lookup_field = "pk"
