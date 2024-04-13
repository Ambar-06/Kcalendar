import datetime
from common.boilerplate.auth.password_handler import PasswordHandler
from common.boilerplate.input_output_operations.datetime import DateTime
from common.boilerplate.services.base_service import BaseService
from common.helper.constants import StatusCodes
from kcalendar import settings
from user.repositories.user_repo import UserRepository
from user.util.registration_validator import RegistrationValidator

class RegisterService(BaseService):
    def __init__(self):
        self.date_util = DateTime()
        self.user_repo = UserRepository()
        self.register_validator = RegistrationValidator()
        self.pw_handler = PasswordHandler()

    def post_service(self, request, data):
        today = datetime.datetime.now()
        self.register_validator.validate(request, data)
        values = {
            'username': data.get("userName"),
            'email': data.get("email"),
            'first_name': data.get("firstName"),
            'last_name': data.get("lastName"),
            'password': self.pw_handler.hash_pw(data.get("password")),
            "token_expiry": self.date_util.change_time(today, operation="+", delta={"days": int(settings.USER_TOKEN_EXPIRY)}, time_zone="Asia"),
        }
        user_data = self.user_repo.Create(values)
        return self.ok(user_data, StatusCodes().SUCCESS)
        
