from common.boilerplate.models.base_model import BaseModel
from django.db import models

class Invite(BaseModel):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    platform = models.IntegerField(null=True, blank=True)
    duration_in_minutes = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

