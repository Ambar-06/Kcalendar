from common.boilerplate.db.base_repository import BaseRepository
from invite.models.invitation import Invitation


class InvitationRepository(BaseRepository):
    def __init__(self):
        self.model = Invitation