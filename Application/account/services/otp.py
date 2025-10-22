import random
import string
from datetime import timedelta

from django.utils import timezone

from account.exceptions import InvalidOtpCodeError
from account.models import OTP, User


class OTPService:
    def __init__(self, otp_model: type[OTP] = OTP):
        self.otp_model = otp_model

    def generate_otp(self, user: User) -> OTP:
        """
        This method is responsible for generating an OTP code for the user account.
        If there is an unexpired code, it returns the same.
        """
        otp = self.otp_model.objects.filter(user=user).first()

        if otp and not otp.is_expired():
            return otp

        expired_at = timezone.now() + timedelta(minutes=2)

        return self.otp_model.objects.create(user=user, code=self._generate_code, expired_at=expired_at)

    def check_otp(self, phone_number: str, otp_code: str) -> bool:
        """
        This method is responsible for checking the sent code and whether it matches the desired number.
        If the code is correct, the response is 'True', otherwise the corresponding error is raised.
        After the code is verified, the code is deleted from the database.
        """
        try:
            otp = self.otp_model.objects.select_related("user").get(user__phone_number=phone_number, code=otp_code)
        except self.otp_model.DoesNotExist:
            raise InvalidOtpCodeError()

        if otp.is_expired():
            raise InvalidOtpCodeError()

        otp.delete()

        return True

    @property
    def _generate_code(self):
        """
        This method is responsible for generating a 6-digit code.
        """
        return ''.join(random.choices(string.digits, k=6))
