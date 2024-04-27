import datetime as dt
import json
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import WebApplicationClient
from dateutil import parser
from google.apps import meet_v2 as meet
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from common.helper.constants import Platform
from common.helper.unique_id_generator import RandomIDNumberGenerator
from kcalendar import settings
from user.repositories.auth_repo import AuthRepository
from user.repositories.user_repo import UserRepository
from google.auth.exceptions import RefreshError

SCOPES = [settings.READ_ONLY_CAL, settings.CAL, settings.MEETING_SPACE]
CREDS = {
    "installed": {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "project_id": settings.PROJECT_ID,
        "auth_uri": settings.AUTH_URI,
        "token_uri": settings.TOKEN_URI,
        "auth_provider_x509_cert_url": settings.AUTH_PROVIDER_X509_CERT_URL,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"],
    }
}

class GoogleClient:
    def __init__(self):
        self.auth_repo = AuthRepository()
        self.user_repo = UserRepository()
  
    def create_service(self, user_id : str = None, return_creds : bool = False):
        if not user_id:
            creds = Credentials(token_uri=settings.TOKEN_URI, client_id=settings.GOOGLE_CLIENT_ID, client_secret=settings.GOOGLE_CLIENT_SECRET, scopes=SCOPES)
        else:
            user_ins = self.user_repo.GetFirst([("uuid", user_id)], error=False)
            user_token_ins = self.auth_repo.GetFirst([("inviter__uuid", user_id), ("platform", Platform().GOOGLE_MEET)], error=False)
            if user_token_ins:
                creds = Credentials(token=user_token_ins.access_token, refresh_token=user_token_ins.refresh_token, scopes=SCOPES)
                if creds.expired:
                    creds.refresh(Request())
                else:
                    return build("calendar", "v3", credentials=creds)
            config = {
                "installed": {
                    "client_id": settings.GOOGLE_CLIENT_ID,
                    "project_id": settings.PROJECT_ID,
                    "auth_uri": settings.AUTH_URI,
                    "token_uri": settings.TOKEN_URI,
                    "auth_provider_x509_cert_url": settings.AUTH_PROVIDER_X509_CERT_URL,
                    "client_secret": settings.GOOGLE_CLIENT_SECRET,
                    "redirect_uris": ["http://127.0.0.1", "http://localhost"],
                }
            }
            flow = InstalledAppFlow.from_client_config(
            config, SCOPES
            )
            creds_info = flow.run_local_server(port=8001)
            creds_dict = creds_info.to_json()
            creds_dict = json.loads(creds_dict)
            values = {
                "inviter": user_ins,
                "access_token": creds_dict.get("token"),
                "refresh_token": creds_dict.get("refresh_token"),
                "expires_at": creds_dict.get("expiry"),
                "platform": Platform().GOOGLE_MEET
            }
            user_tokens = self.auth_repo.CreateOrUpdate([("inviter__uuid", user_id), ("platform", Platform().GOOGLE_MEET)], values)
            creds = Credentials(token=user_tokens.access_token, refresh_token=user_tokens.refresh_token, scopes=SCOPES)
            if return_creds:
                return creds
        return build("calendar", "v3", credentials=creds)


    def create_event(self, service, event, invitation): 
        try: 
            event = service.events().insert(calendarId='primary', body=event).execute()
        except RefreshError:
            creds = self.create_service(user_id=invitation.inviter.uuid, return_creds=True)
            service = build("calendar", "v3", credentials=creds)
            event = service.events().insert(calendarId='primary', body=event).execute()
        link = event.get('htmlLink')
        invitation.invitation_link = link
        invitation.save()
        return link

    def initialize_event(self, **kwargs):
        
        start_date_time_obj = parser.parse(kwargs.get("start_date_time")) if isinstance(kwargs.get("start_date_time"), str) else kwargs.get("start_date_time")
        end_date_time_obj = start_date_time_obj + dt.timedelta(minutes=30)
        start_time_tz = str(start_date_time_obj).split("+")[0].replace(" ", "T") + "Z"
        end_time_tz = str(end_date_time_obj).split("+")[0].replace(" ", "T") + "Z"

        return {
          'summary': kwargs.get("summary"),
          'location': kwargs.get("location"),
          'description': kwargs.get("description"),
          'start': {
            'dateTime': start_time_tz,
            'timeZone': kwargs.get("timezone"),
          },
          'end': {
            'dateTime': end_time_tz,
            'timeZone': kwargs.get("timezone"),
          },
          'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
          ],
          'attendees': [
            {'email': email } for email in kwargs.get("invitees_list")
          ],
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60},
              {'method': 'popup', 'minutes': 10},
            ],
          },
          'conferenceData': {
            'createRequest': {
                'requestId': RandomIDNumberGenerator().generate_random_id_number(use_alphanumeric=True),
            },
            },
        }
    
    def get_events(self, service):
        now = dt.datetime.utcnow().isoformat() + "Z"
        print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            return {"events" : None}

        events_dict = {"events": []}
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            events_dict.get("events").append({start : event["summary"]})
        return events_dict


    async def create_space(self, creds):
        client = meet.SpacesServiceAsyncClient(credentials=creds)

        request = meet.CreateSpaceRequest()
        response = await client.create_space(request=request)
        
    def create_oauth_uri(self):
        oauth = OAuth2Session(settings.GOOGLE_CLIENT_ID, scope=SCOPES, redirect_uri=["http://127.0.0.1", "http://localhost"])
        authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
        authorization_url, state = oauth.authorization_url(authorization_base_url, access_type='offline')
        return authorization_url, state