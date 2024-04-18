from msgraph import GraphServiceClient
from msgraph.generated.communications.online_meetings import online_meetings_request_builder
from azure.identity import DeviceCodeCredential
import requests
from kcalendar import settings

BASE_URL = settings.MICROSOFT_BASE_URL

scopes = []

tenant_id = ""

client_id = ""

credential = DeviceCodeCredential(
    tenant_id=tenant_id,
    client_id=client_id)
class TeamsClient:
    def __init__(self):
        pass

    def setup_client(self):
        return GraphServiceClient(credential, scopes)
        # request_body = online_meetings_request_builder(
        #     start_date_time = "2019-07-12T14:30:34.2444915-07:00",
        #     end_date_time = "2019-07-12T15:00:34.2464912-07:00",
        #     subject = "User Token Meeting",
        # )
        # result = graph_client.me.calendar.get()

    def initialize_event(self, subject, content, start_date_time, end_date_time, time_zone, location, attendees_list):
        return {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": content
            },
            "start": {
                "dateTime": start_date_time,
                "timeZone": time_zone
            },
            "end": {
                "dateTime": end_date_time,
                "timeZone": time_zone
            },
            "location":{
                "displayName":location
            },
            "attendees": [
                {
                "emailAddress": {
                    "address":email,
                    "name": ""
                },
                "type": "required"
                }  for email in attendees_list
            ],
            "allowNewTimeProposals": True,
            "isOnlineMeeting": True,
            "onlineMeetingProvider": "teamsForBusiness"
        }

    def send_meeting_invite(self, event):
        url = BASE_URL + "/v1.0/me/calendar"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, body=event, headers=headers)
        return response