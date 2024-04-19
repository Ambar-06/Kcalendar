from rest_framework import serializers

from common.boilerplate.input_output_operations.datetime import DateTimeFormatter
from common.helper.constants import PlatformDictionary
from invite.models.invitation import Invitation

class InvitationFilterSerializer(serializers.Serializer):
    meetingDateTime = serializers.DateTimeField(required=True, allow_null=False,
        input_formats=[DateTimeFormatter().DATE_TIME_FORMAT_2], error_messages={
        'required': 'Meeting time is required',
        'null': 'Meeting time cannot be null'
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
    isPassRequired = serializers.BooleanField(required=False, default=False, error_messages={
        'required': 'Pass code requirement is required'
    })

class InviteViewSerializer(serializers.ModelSerializer):
    invitationId = serializers.UUIDField(source='uuid', read_only=True)
    invitationDateTime = serializers.DateTimeField(source='invitation_date_time', read_only=True)
    invitationLink = serializers.URLField(source='invitation_link', read_only=True)
    invitationUniqueId = serializers.CharField(source='invitation_unique_id', read_only=True)
    class Meta:
        model = Invitation
        fields = [
            'invitationId',
            'invitationDateTime',
            'invitationLink',
            'invitationUniqueId'
        ]