from common.boilerplate.services.base_service import BaseService
from common.helper.constants import StatusCodes
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
        invitation = self.invitation_repo.Create(values)
        service = self.google_client.create_service(user_id=request.user.uuid)
        invite = self.google_client.initialize_event(invitees_list=invitation.invitees_emails, start_time=invitation.time, end_time=invitation.time, description="Meeting", location="Online", summary="Meeting", timezone="Asia/Kolkata")
        self.google_client.create_event(service, invite)
        return self.ok(invitation, StatusCodes().SUCCESS)

        