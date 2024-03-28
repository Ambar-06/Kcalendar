from django.db import models
from common.boilerplate.models.base_model import BaseModel
from user.models.user import User

class Invitation(BaseModel):

    date = models.DateField()
    time = models.TimeField()
    inviter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='inviter', null=True)
    is_invitee_notified = models.BooleanField(default=False, null=True, blank=True)
    is_inviter_notified = models.BooleanField(default=False, null=True, blank=True)
    invite_status = models.IntegerField(null=True, blank=True)
    reschedule_invite_id = models.UUIDField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    is_expired = models.BooleanField(default=False, null=True, blank=True)
    invitees_count = models.IntegerField(default=0, null=True, blank=True)
    invitees_emails = models.TextField(null=True, blank=True)

