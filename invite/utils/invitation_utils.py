from invite.google.google_client import GoogleClient


class InvitationUtil:
    def __init__(self):
        self.google_client = GoogleClient()

    def send_google_meet_invite(self, request, invitation, invitees_list, start_date_time, description, location, summary, timezone):
        service = self.google_client.create_service(user_id=request.user.get("uuid"))
        invite = self.google_client.initialize_event(invitees_list=invitees_list, start_date_time=start_date_time, description=description, location=location, summary=summary, timezone=timezone)
        self.google_client.create_event(service, invite, invitation)