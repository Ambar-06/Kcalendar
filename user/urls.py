from django.urls import path

from .views import *

urlpatterns = [
    path('register', RegisterViews.as_view(), name='register'),
    path('generate-auth-token/<str:userId>', GenerateAuthTokenViews.as_view(), name='generate-auth-token'),
]