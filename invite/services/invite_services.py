from common.boilerplate.services.base_service import BaseService
from common.helper.constants import Platform, StatusCodes
from invite.google.google_client import GoogleClient
from invite.repositories.invitation_repo import InvitationRepository
from invite.utils.invitation_utils import InvitationUtil
from user.repositories.user_repo import UserRepository


class InviteService(BaseService):
    def __init__(self):
        self.invitation_repo = InvitationRepository()
        self.invitation_util = InvitationUtil()
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
        if int(data.get("platform")) == Platform().GOOGLE_MEET:
            self.invitation_util.send_google_meet_invite(request, invitation, data.get("meetingInvitees"), data.get("meetingDateTime"), "Meeting", "Online", "Meeting", "GMT+05:30")
        elif int(data.get("platform")) == Platform().ZOOM:
            pass
        elif int(data.get("platform")) == Platform().MICROSOFT_TEAMS:
            self.invitation_util.send_teams_meet_invite(request, invitation, data.get("meetingInvitees"), data.get("meetingDateTime"), "Meeting", "Online", "Meeting", "GMT+05:30", is_pass_code_required=False)
        return self.ok(invitation, StatusCodes().SUCCESS)

        