from django.urls import path

from . import views

AUTHENTICATION_URLs = [
    path("sent-otp/", views.SentOTPView.as_view(), name="sent-otp"),
    path("verify-otp/", views.VerifyOTPView.as_view(), name="verify-otp"),
]

DASHBOARD_URLs = [
    path("", views.GetListUserView.as_view(), name="get-users-account"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/<str:pk>/", views.OtherUserProfileView.as_view(), name="user-profile"),
]

urlpatterns = AUTHENTICATION_URLs + DASHBOARD_URLs
