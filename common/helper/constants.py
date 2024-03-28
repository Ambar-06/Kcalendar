from dataclasses import dataclass


@dataclass
class Platform:
    def __init__(self):
        self.GOOGLE_MEET = 1
        self.ZOOM = 2
        self.MICROSOFT_TEAMS = 3
        self.WEBEX = 4

obj_platform = Platform()
PlatformDictionary = obj_platform.__dict__

@dataclass
class InviteStatus:
    def __init__(self):
        self.PENDING = 1
        self.ACCEPTED = 2
        self.REJECTED = 3
        self.CANCELLED = 4
        self.RESCHEDULED = 5

obj_invite_status = InviteStatus()
InviteStatusDictionary = obj_invite_status.__dict__

@dataclass
class InviteType:
    def __init__(self):
        self.SCHEDULED = 1
        self.IMMEDIATE = 2

obj_invite_type = InviteType()
InviteTypeDictionary = obj_invite_type.__dict__