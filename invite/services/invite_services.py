from common.boilerplate.services.base_service import BaseService
from invite.repositories.invitation_repo import InvitationRepository


class InviteService(BaseService):
    def __init__(self):
        self.invitation_repo = InvitationRepository()

    def post_service(self, request, data):
        ...