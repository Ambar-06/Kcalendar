import requests
from common.boilerplate.input_output_operations.datetime import DateTime
from kcalendar import settings
from dateutil import parser

BASE_URL = settings.MICROSOFT_BASE_URL


class TeamsClient:
    def __init__(self):
        pass

    def initialize_event(
        self,
        subject,
        content,
        start_date_time,
        time_zone,
        location,
        attendees_list,
    ):
        end_date_time = DateTime().change_time(parser.parse(start_date_time), delta={"minutes" : 30})
        # return {
        #     "subject": subject,
        #     "body": {"contentType": "HTML", "content": content},
        #     "start": {"dateTime": start_date_time, "timeZone": time_zone},
        #     "end": {"dateTime": end_date_time, "timeZone": time_zone},
        #     "location": {"displayName": location},
        #     "attendees": [
        #         {"emailAddress": {"address": email, "name": ""}, "type": "required"}
        #         for email in attendees_list
        #     ],
        #     "allowNewTimeProposals": True,
        #     "isOnlineMeeting": True,
        #     "onlineMeetingProvider": "teamsForBusiness",
        # }
        return {
            "subject": "Meeting for New Member",
            "body": {
                "contentType": "HTML",
                "content": "Hello Team"
            },
            "start": {
                "dateTime": start_date_time,
                "timeZone": "Pacific Standard Time"
            },
            "end": {
                "dateTime": str(end_date_time),
                "timeZone": "Pacific Standard Time"
            },
            "location":{
                "displayName":"Virtual"
            },
            "attendees": [
                {
                "emailAddress": {
                    "address":"brannstrom9911@gmail.com",
                    "name": "User"
                },
                "type": "required"
                }
            ],
            "allowNewTimeProposals": True,
            "isOnlineMeeting": True,
            "onlineMeetingProvider": "teamsForBusiness"
            }

    def send_meeting_invite(self, event, is_pass_code_required: bool = False):
        if is_pass_code_required:
            event.update({"joinMeetingIdSettings": {"isPasscodeRequired": True}})
        # url = BASE_URL + "v1.0/me/calendar"
        url = BASE_URL + "v1.0/me/events"
        headers = {"Content-Type": "application/json"}
        print(event)
        response = requests.post(url, data=event, headers=headers)
        print(response)
        print(response.text)
        return response
