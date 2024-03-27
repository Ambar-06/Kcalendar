from django.db import models

from common.boilerplate.models.base_model import BaseModel

class User(BaseModel):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255, null=True, blank=True)
    