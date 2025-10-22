from rest_framework_simplejwt.tokens import RefreshToken

from account.exceptions import UserNotFoundError
from account.models import User


class UserHelper:
    def __init__(self):
        self.model = User

    def get_user(self, **kwargs):
        """
        This method is responsible for finding the user with the properties that are sent.
        If the user is not found, an error is raised.
        """
        try:
            return self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            raise UserNotFoundError()

    @staticmethod
    def generate_token(user: User):
        """
        This method is responsible for creating a JWT token for a user account.
        """
        token = RefreshToken.for_user(user)
        return {"tokens": {"access": str(token.access_token), "refresh": str(token)}}
