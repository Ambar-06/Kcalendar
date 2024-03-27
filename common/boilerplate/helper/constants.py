from dataclasses import dataclass


@dataclass
class Platform:
    def __init__(self):
        self.GOOGLE_MEET = 1
        self.ZOOM = 2
        self.MICROSOFT_TEAMS = 3
        self.WEBEX = 4