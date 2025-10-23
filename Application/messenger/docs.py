from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse

from .presentation.serializers.input import CreatePrivateConversationSerializer
from .presentation.serializers.output import ConversationDataSerializer, ConversationDetailDataSerializer

CreatePrivateConversationViewDoc = extend_schema_view(
    post=extend_schema(
        summary="Create new private conversation",
        description="This API is used to create a new private conversation.",
        tags=["Conversation"],
        request=CreatePrivateConversationSerializer,
        responses={
            200: OpenApiResponse(
                response=ConversationDataSerializer,
                description="Create new conversation successfully"
            ),
        },
    ),
)

ConversationListViewDoc = extend_schema_view(
    get=extend_schema(
        summary="Get conversation list",
        description="This API is used to get conversation list.",
        tags=["Conversation Data"],
        responses={
            200: OpenApiResponse(
                response=ConversationDataSerializer,
                description="Get conversation list successfully"
            ),
        },
    ),
)

ConversationDetailViewDoc = extend_schema_view(
    get=extend_schema(
        summary="Get conversation detail",
        description="This API is used to get conversation detail.",
        tags=["Conversation Data"],
        responses={
            200: OpenApiResponse(
                response=ConversationDetailDataSerializer,
                description="Get conversation detail"
            ),
        },
    ),
)
