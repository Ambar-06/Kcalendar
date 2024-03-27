from common.boilerplate.db.base_repository import BaseRepository
from user.models.user import User


class UserRepository(BaseRepository):
    def __init__(self):
        self.model = User