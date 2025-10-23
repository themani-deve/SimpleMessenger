from django.urls import path

from . import views

CONVERSATION_URLs = [
    path("new/private/", views.CreatePrivateConversationView.as_view(), name="new-private-conversation"),
]

CONVERSATION_DATA_URLs = [
    path("", views.ConversationListView.as_view(), name="conversation-list"),
    path("<uuid:conversation_id>/", views.ConversationDetailView.as_view(), name="conversation-detail"),
]

urlpatterns = CONVERSATION_URLs + CONVERSATION_DATA_URLs
