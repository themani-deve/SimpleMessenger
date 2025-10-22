from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse

from core.base_serializer import DetailResponseSerializer
from .presentation.serializers.input import SentOtpSerializer, LoginSerializer
from .presentation.serializers.output import TokenDataSerializer, ProfileDataSerializer, ProfileAttributeSerializer

SentOtpViewDoc = extend_schema_view(
    post=extend_schema(
        summary="Send OTP code",
        description="This API is used to send OTP code to user's mobile number.",
        tags=["Authentication"],
        request=SentOtpSerializer,
        responses={
            200: OpenApiResponse(response=DetailResponseSerializer, description="Code sent successfully."),
        }
    ),
)

LoginViewDoc = extend_schema_view(
    post=extend_schema(
        summary="Check the OTP code",
        description="This API is used to check the code entered for the login operation.",
        tags=["Authentication"],
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(response=TokenDataSerializer, description="User successfully logged in."),
        }
    ),
)

ProfileViewDoc = extend_schema_view(
    get=extend_schema(
        summary="Get user profile",
        description="This API is used to get user profile information.",
        tags=["Dashboard"],
        responses={
            200: OpenApiResponse(response=ProfileDataSerializer, description="User profile information."),
        }
    ),
    patch=extend_schema(
        summary="Update user profile",
        description="This API is used to update user profile information.",
        tags=["Dashboard"],
        request=ProfileAttributeSerializer,
        responses={
            200: OpenApiResponse(response=ProfileDataSerializer, description="User profile updated successfully."),
        }
    ),
)

OtherUserProfileViewDoc = extend_schema_view(
    get=extend_schema(
        summary="Get other user profile",
        description="This API is used to get other user profile information.",
        tags=["Dashboard"],
        responses={
            200: OpenApiResponse(response=ProfileDataSerializer, description="User profile information."),
        }
    )
)
