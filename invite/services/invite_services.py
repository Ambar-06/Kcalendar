from common.boilerplate.services.base_service import BaseService
from invite.google.google_client import GoogleClient
from invite.repositories.invitation_repo import InvitationRepository


class InviteService(BaseService):
    def __init__(self):
        self.invitation_repo = InvitationRepository()
        self.google_client = GoogleClient()

    def post_service(self, request, data):
        values = {
            "date" : data.get("meetingDate"),
            "time" : data.get("meetingTime"),
            "inviter" : request.user,
            "invitees_count" : len(data.get("meetingInvitees")),
            "invitees_emails" : data.get("meetingInvitees"),
        }    
        invite = self.invitation_repo.Create(values)

        