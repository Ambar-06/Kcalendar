import bcrypt

"""
PasswordHandler is a class that handles password hashing and password validation.
Fields:
Methods:
    hash_pw: This method is used to hash the password
    is_password_valid: This method is used to check if the password is valid
WorkFlow:
    First we check if the password is empty or not
    If the password is empty then we return None
    Then we hash the password
    Then we return the hashed password
    First we check if the password or hashed password is empty or not
    If the password or hashed password is empty then we return False
    Then we check if the password is valid or not
    Then we return the response
"""


class PasswordHandler:
    def __init__(self):
        pass

    def hash_pw(self, password) -> str:
        if not password:
            return None
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password.decode("utf-8")

    def is_password_valid(self, password, hashed_password) -> bool:
        if not password or not hashed_password:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
