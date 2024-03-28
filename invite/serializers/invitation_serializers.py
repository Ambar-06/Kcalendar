from rest_framework import serializers

class InvitationFilterSerializer(serializers.Serializer):
    meetingTime = serializers.TimeField(required=True, allow_null=False, error_messages={
        'required': 'Meeting time is required',
        'null': 'Meeting time cannot be null'
    })
    meetingDate = serializers.DateField(required=True, allow_null=False, error_messages={
        'required': 'Meeting date is required',
        'null': 'Meeting date cannot be null'
    })
    invitees = serializers.ListField(child=serializers.EmailField(), required=True, allow_empty=False, error_messages={
        'required': 'Invitees are required',
        'empty': 'Invitees cannot be empty'
    })
    