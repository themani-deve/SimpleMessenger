from django.urls import path

from . import views

AUTHENTICATION_URLs = [
    path("sent-otp/", views.SentOtpView.as_view(), name="sent-otp"),
    path("login/", views.LoginView.as_view(), name="login"),
]

DASHBOARD_URLs = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/<str:pk>/", views.OtherUserProfileView.as_view(), name="user-profile"),
]

urlpatterns = AUTHENTICATION_URLs + DASHBOARD_URLs
