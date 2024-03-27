import requests
from django.conf import settings

"""
This class is used for google login
Fields:
    baseurl: Base url for google login
    clientId: Client id for google login
    clientSecret: Client secret for google login
Methods:
    authenticate: This method is used for authenticating a user
WorkFlow:
    First we get the url
    Then we make a get request to the url
    Then we return the response
"""


class GoogleLogin:
    def __init__(self):
        self.baseurl = "https://oauth2.googleapis.com/tokeninfo?"
        self.clientId = settings.GOOGLE_CLIENT_ID
        self.clientSecret = settings.GOOGLE_CLIENT_SECRET

    def authenticate(self, id_token):
        url = self.baseurl + "id_token=" + id_token

        response = requests.get(
            url, headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

        data = response.json()
        return data
