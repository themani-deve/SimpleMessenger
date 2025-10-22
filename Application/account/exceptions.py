from rest_framework import status

from core.base_exception import DomainException


class UserNotFoundError(DomainException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User not found"
    default_code = "user_not_found"


class InvalidOtpCodeError(DomainException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid OTP Code"
    default_code = "invalid_otp_code"
