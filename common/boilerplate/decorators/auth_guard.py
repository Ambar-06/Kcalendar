import typing as _
from rest_framework.response import Response
from jose import jwt
from common.helpers.constants import UserStatus
from common.boilerplate.auth.jwt_service import JWTService
from user.models.user import User
from user.repositories.user_repo import UserRepository

"""
This class is used for validating the user
This class is inherited from BaseService
Fields:
    userRepo: Instance of UserRepository
Methods:
    validate_auth_user: This method is used for validating the user
WorkFlow:
    First we get the authorization header
    Then we check if the authorization header is present or not
    If the authorization header is not present then we raise an exception
    If the authorization header is present then we get the jwt token
    Then we check if the jwt token is present or not
    If the jwt token is not present then we raise an exception
    Then we verify the jwt token
    Then we check if the payload is present or not
    If the payload is not present then we raise an exception
    Then we get the user object
    Then we check if the user object is present or not
    If the user object is not present then we raise an exception
    Then we check if the user is an active user or not
    If the user is not an active user then we raise an exception
    Then we return the response
"""
NOT_VALID_TOKEN = Response(
    {
        "success": False,
        "code": 401,
        "message": "Please provide a valid authorization header",
    },
    status=401,
)

NOT_VALID_ROLE = Response(
    {"success": False, "code": 401, "message": "You don't have access permission"},
    status=401,
)

NOT_ACTIVE_USER = Response(
    {"success": False, "code": 401, "message": "User is an inactive user"}, status=401
)

HEADER_NOT_FOUND = Response(
    {"success": False, "code": 401, "message": "Authorization header not present"},
    status=401,
)

EXPIRED_TOKEN = Response(
    {"success": False, "code": 408, "message": "Token is expired"}, status=408
)

WRONG_SIGNATURE = Response(
    {"success": False, "code": 401, "message": "Invalid signature"}, status=401
)


def auth_guard(roles=None):
    def validate_auth_user(fun: _.Callable):
        jwt_service = JWTService()
        user_repository = UserRepository()

        def inner(*args, **kwargs):
            req = args[1]
            auth_header = req.headers.get("Authorization")
            if not auth_header:
                return HEADER_NOT_FOUND

            jwt_token = auth_header.replace("Bearer ", "")
            if not jwt_token:
                return NOT_VALID_TOKEN

            try:
                payload = jwt_service.verify_token(jwt_token)
            except jwt.ExpiredSignatureError:
                return EXPIRED_TOKEN
            except jwt.JWTError:
                return WRONG_SIGNATURE
            if not payload:
                return NOT_VALID_TOKEN

            sub: _.Optional[str] = payload.get("sub")

            user: _.Optional[User] = user_repository.GetFirst(
                [("uuid", sub)], error=False
            )
            if not user:
                return NOT_VALID_TOKEN
            if roles and not user.role in roles:
                return NOT_VALID_ROLE
            if user.is_deleted:
                return NOT_VALID_TOKEN
            if user.status == UserStatus().INACTIVE:
                return NOT_ACTIVE_USER
            req.user = user.__dict__
            return fun(*args, user, payload, **kwargs)

        return inner

    return validate_auth_user
