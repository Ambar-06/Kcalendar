from common.boilerplate.db.base_repository import BaseRepository
from user.models import AuthTokens

class AuthRepository(BaseRepository):
    def __init__(self):
        self.model = AuthTokens