from user.repositories.auth_repo import AuthRepository
from user.repositories.user_repo import UserRepository
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from kcalendar import settings
from user.repositories.auth_repo import AuthRepository
from user.repositories.user_repo import UserRepository

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

class GoogleClientClassic:
    def __init__(self):
        self.auth_repo = AuthRepository()
        self.user_repo = UserRepository()

    def authorize(self) -> Credentials:  
        """Ensure valid credentials for calling the Meet REST API."""
        CONFIG = CREDS
        credentials = None

        if os.path.exists('token.json'):
            credentials = Credentials.from_authorized_user_file('token.json')

        if credentials is None:
            flow = InstalledAppFlow.from_client_config(
                CONFIG,
                scopes=SCOPES)
            flow.run_local_server(port=0)
            credentials = flow.credentials

        if credentials and credentials.expired:
            credentials.refresh(Request())

        if credentials is not None:
            with open("token.json", "w") as f:
                f.write(credentials.to_json())

        return credentials