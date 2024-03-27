import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from common.boilerplate.helper.constants import Platform
from kcalendar import settings
from user.repositories.auth_repo import AuthRepository
from user.repositories.user_repo import UserRepository

SCOPES = [settings.READ_ONLY_CAL, settings.CAL]

class GoogleClient:
  def __init__(self):
    self.auth_repo = AuthRepository()
    self.user_repo = UserRepository()
  
  def create_service(self, parent=True, user_id : str = None ):
    if parent:
        creds = Credentials(token_uri=settings.TOKEN_URI, client_id=settings.GOOGLE_CLIENT_ID, client_secret=settings.GOOGLE_CLIENT_SECRET, scopes=SCOPES)
    else:
      user_tokens = self.auth_repo.GetFirst([("invitee__uuid", user_id), ("platform", Platform().GOOGLE_MEET)], error=False)
      if not user_tokens:
        flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
        )
        creds_info = flow.run_local_server(port=0)
        creds_dict = creds_info.to_json()
        user_ins = self.user_repo.GetFirst([("uuid", user_id)], error=False)
        values = {
            "inviter": user_ins,
            "access_token": creds_dict.get("token"),
            "refresh_token": creds_dict.get("refresh_token"),
            "expires_at": creds_dict.get("expiry"),
            "platform": Platform().GOOGLE_MEET
        }
        creds = Credentials(token=user_tokens.access_token, refresh_token=user_tokens.refresh_token, scopes=SCOPES)
    return build("calendar", "v3", credentials=creds)



def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
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
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()

  # Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

# event = service.events().insert(calendarId='primary', body=event).execute()
# print 'Event created: %s' % (event.get('htmlLink'))
