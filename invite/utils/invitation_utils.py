from invite.google.google_client import GoogleClient
from invite.microsoft_teams.teams_client import TeamsClient


class InvitationUtil:
    def __init__(self):
        self.google_client = GoogleClient()
        self.microsoft_client = TeamsClient()

    def send_google_meet_invite(
        self,
        request,
        **kwargs
    ):
        service = self.google_client.create_service(user_id=request.user.get("uuid"))
        invite = self.google_client.initialize_event(
            invitees_list=kwargs.get("invitees_list"),
            start_date_time=kwargs.get("start_date_time"),
            description=kwargs.get("description"),
            location=kwargs.get("location"),
            summary=kwargs.get("summary"),
            timezone=kwargs.get("timezone"),
        )
        self.google_client.create_event(service, invite, invitation=kwargs.get("invitation"))

    def send_teams_meet_invite(
        self,
        request,
        invitation,
        invitees_list,
        start_date_time,
        description,
        location,
        summary,
        timezone,
        is_pass_code_required: bool = False,
    ):
        event = self.microsoft_client.initialize_event(
            subject=description,
            content=summary,
            start_date_time=start_date_time,
            time_zone=timezone,
            location=location,
            attendees_list=invitees_list,
        )
        self.microsoft_client.send_meeting_invite(event, is_pass_code_required)
