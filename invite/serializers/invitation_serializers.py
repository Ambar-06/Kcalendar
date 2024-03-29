from rest_framework import serializers

from common.helper.constants import PlatformDictionary

class InvitationFilterSerializer(serializers.Serializer):
    meetingTime = serializers.TimeField(required=True, allow_null=False, error_messages={
        'required': 'Meeting time is required',
        'null': 'Meeting time cannot be null'
    })
    meetingDate = serializers.DateField(required=True, allow_null=False, error_messages={
        'required': 'Meeting date is required',
        'null': 'Meeting date cannot be null'
    })
    meetingInvitees = serializers.ListField(child=serializers.EmailField(), required=True, allow_empty=False, error_messages={
        'required': 'Invitees are required',
        'empty': 'Invitees cannot be empty'
    })
    platform = serializers.ChoiceField(choices=list(PlatformDictionary.values()), required=True, allow_null=False, error_messages={
        'required': 'Platform is required',
        'null': 'Platform cannot be null'
    })
    meetingTitle = serializers.CharField(required=True, allow_blank=False, error_messages={
        'required': 'Meeting title is required',
        'blank': 'Meeting title cannot be blank'
    })
    meetingDescription = serializers.CharField(required=True, allow_blank=False, error_messages={
        'required': 'Meeting description is required',
        'blank': 'Meeting description cannot be blank'
    })
    meetingDuration = serializers.IntegerField(required=True, allow_null=False, error_messages={
        'required': 'Meeting duration is required',
        'null': 'Meeting duration cannot be null'
    })
