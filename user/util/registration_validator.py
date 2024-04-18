from rest_framework import exceptions

from common.helper.constants import StatusCodes
from user.repositories.user_repo import UserRepository

class RegistrationValidator:
    def __init__(self):
        self.user_repository = UserRepository()

    def validate(self, request, data):
        user_by_username = self.user_repository.GetFirst([("username", data.get("userName"))], error=False)
        user_by_email = self.user_repository.GetFirst([("email", data.get("email"))], error=False)
        if user_by_username or user_by_email:
            raise exceptions.APIException("User Name or Email already exists", code=StatusCodes().BAD_REQUEST)