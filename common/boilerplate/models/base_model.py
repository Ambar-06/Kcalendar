from django.db import models
import uuid

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        get_latest_by = "updated_at"
        abstract = True