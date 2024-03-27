from django.db import models

from common.boilerplate.models.base_model import BaseModel

class User(BaseModel):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255, null=True, blank=True)

class AuthTokens(BaseModel):
    invitee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user_auth_tokens", null=True)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    expires_at = models.DateTimeField()
    platform = models.IntegerField()
    