from django.urls import path
from .views import *

urlpatterns = [
    path('send', InviteViews.as_view(), name='invite'),
]
