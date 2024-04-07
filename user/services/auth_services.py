from common.boilerplate.auth.jwt_service import JWTService
from common.boilerplate.services.base_service import BaseService
from common.helper.constants import StatusCodes
from user.repositories.user_repo import UserRepository
from kcalendar import settings

class GenerateAuthTokenService(BaseService):
    def __init__(self):
        self.user_repo = UserRepository()
        self.jwt_service = JWTService()

    def get_service(self, request, data):
        user_ins = self.user_repo.GetFirst([("uuid", data.get("userId"))])
        token = self.jwt_service.create_token(user_ins, expiry=int(settings.JWT_EXPIRATION_IN_DAYS))
        return self.ok({"token": token}, StatusCodes().SUCCESS)