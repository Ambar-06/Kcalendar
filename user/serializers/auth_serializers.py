from rest_framework import serializers

class GenerateAuthTokenSerializer(serializers.Serializer):
    userId = serializers.UUIDField(required=True, allow_null=False, error_messages={
        'required': 'User Id is required',
        'null': 'User Id cannot be null'
    })