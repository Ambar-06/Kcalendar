from rest_framework import serializers

from user.models.user import User


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

class UserViewSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source="username", read_only=True)
    firstName = serializers.CharField(source="first_name", read_only=True)
    lastName = serializers.CharField(source="last_name", read_only=True)
    email = serializers.EmailField(read_only=True)
    token = serializers.UUIDField(read_only=True)
    tokenExpiry = serializers.DateTimeField(source="token_expiry", read_only=True)
    class Meta:
        model = User
        fields = [
            "userName",
            "firstName",
            "lastName",
            "email",
            "token",
            "tokenExpiry"
        ]