from django.db import models
from common.boilerplate.models.base_model import BaseModel
from user.models.user import User

class Invitation(BaseModel):

    date = models.DateField()
    time = models.TimeField()
    inviter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='inviter')
    is_invitee_notified = models.BooleanField(default=False, null=True, blank=True)
    is_inviter_notified = models.BooleanField(default=False, null=True, blank=True)
    is_accepted = models.BooleanField(default=False, null=True, blank=True)
    is_declined = models.BooleanField(default=False, null=True, blank=True)
    is_cancelled = models.BooleanField(default=False, null=True, blank=True)
    is_rescheduled = models.BooleanField(default=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    is_expired = models.BooleanField(default=False, null=True, blank=True)
    invitees_count = models.IntegerField(default=0, null=True, blank=True)
    invitees_emails = models.TextField(null=True, blank=True)

