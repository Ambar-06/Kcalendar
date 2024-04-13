from common.boilerplate.services.base_service import BaseService
from common.helper.constants import StatusCodes
from invite.google.google_client import GoogleClient
from invite.repositories.invitation_repo import InvitationRepository
from user.repositories.user_repo import UserRepository


class InviteService(BaseService):
    def __init__(self):
        self.invitation_repo = InvitationRepository()
        self.google_client = GoogleClient()
        self.user_repo = UserRepository()

    def post_service(self, request, data):
        user_ins = self.user_repo.GetFirst([("uuid", request.user.get("uuid"))], error=False)
        values = {
            "invitation_date_time" : data.get("meetingDateTime"),
            "inviter" : user_ins,
            "invitees_count" : len(data.get("meetingInvitees")),
            "invitees_emails" : data.get("meetingInvitees"),
        }    
        invitation = self.invitation_repo.Create(values)
        service = self.google_client.create_service(user_id=request.user.get("uuid"))
        invite = self.google_client.initialize_event(invitees_list=invitation.invitees_emails, start_date_time=invitation.invitation_date_time, description="Meeting", location="Online", summary="Meeting", timezone="GMT+05:30")
        self.google_client.create_event(service, invite)
        return self.ok(invitation, StatusCodes().SUCCESS)

        