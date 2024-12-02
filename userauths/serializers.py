from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User  # Ensure `User` model includes a `role` field

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed('Invalid username or password.')

        # Check user's role
        allowed_roles = ['agency', 'authority']
        if user.role not in allowed_roles:
            raise AuthenticationFailed('Only users with roles agency or authority can log in.')

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': user.role,  # Include role in the response
        }
