from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Email is required",
            "null": "Email cannot be null",
            "invalid": "Email is invalid",
        },
    )
    password = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Password is required",
            "null": "Password cannot be null",
        },
    )
    firstName = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "First Name is required",
            "null": "First Name cannot be null",
        },
    )
    lastName = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Last Name is required",
            "null": "Last Name cannot be null",
        },
    )
    userName = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Username is required",
            "null": "Username cannot be null",
        },
    )
