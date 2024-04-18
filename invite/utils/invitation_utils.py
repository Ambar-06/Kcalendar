from invite.google.google_client import GoogleClient
from invite.microsoft_teams.teams_client import TeamsClient


class InvitationUtil:
    def __init__(self):
        self.google_client = GoogleClient()
        self.microsoft_client = TeamsClient()

    def send_google_meet_invite(self, request, invitation, invitees_list, start_date_time, description, location, summary, timezone):
        service = self.google_client.create_service(user_id=request.user.get("uuid"))
        invite = self.google_client.initialize_event(invitees_list=invitees_list, start_date_time=start_date_time, description=description, location=location, summary=summary, timezone=timezone)
        self.google_client.create_event(service, invite, invitation)

    def send_teams_meet_invite(self, request, invitation, invitees_list, start_date_time, description, location, summary, timezone):
        # self.microsoft_client.setup_client()
        event = self.microsoft_client.initialize_event(subject=description, content=summary, start_date_time=start_date_time, end_date_time=start_date_time, time_zone=timezone, location=location, attendees_list=invitees_list)
        self.microsoft_client.send_meeting_invite(event)