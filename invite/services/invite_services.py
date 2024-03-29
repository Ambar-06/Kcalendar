from common.boilerplate.services.base_service import BaseService
from invite.repositories.invitation_repo import InvitationRepository


class InviteService(BaseService):
    def __init__(self):
        self.invitation_repo = InvitationRepository()

    def post_service(self, request, data):        
        values = {
            "user_id": request.user.id,
            "title": data.get("meetingTitle"),
            "date" : data.get("meetingDate"),
            "time": data.get("meetingTime"),
            "description": data.get("meetingDescription"),
            "start_time": data.get("start_time"),
            "end_time": data.get("end_time"),
            "platform": data.get("platform"),
            "invite_type": data.get("invite_type"),
            "invitees": data.get("meetingInvitees"),
            "duration": data.get("meetingDuration"),
        }
        