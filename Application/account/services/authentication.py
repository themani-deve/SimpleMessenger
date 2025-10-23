from account.models import User
from .helper import UserHelper
from .otp import OTPService


class AuthenticationService:
    def __init__(
            self,
            user_helper: type[UserHelper] = UserHelper,
            user_model: type[User] = User,
            otp_service: type[OTPService] = OTPService
    ):
        self.user_helper = user_helper
        self.user_model = user_model
        self.otp_service = otp_service

    def sent_otp(self, phone_number: str) -> dict:
        """
        This method is used to generate OTP code to log in to the user account.
        """
        user = self.user_model.objects.filter(phone_number=phone_number).first()

        if not user:
            user = self.user_model.objects.create_user(phone_number=phone_number)

        self.otp_service().generate_otp(user=user)

        return {"detail": "Code has been sent you."}

    def verify_otp(self, phone_number: str, otp_code: str) -> dict:
        """
        This method is responsible for receiving the OTP code, checking its validity, and as a result
        returning access and refresh tokens.
        """
        user = self.user_model.objects.filter(phone_number=phone_number).first()
        self.otp_service().check_otp(phone_number=phone_number, otp_code=otp_code)

        return self.user_helper.generate_token(user=user)
