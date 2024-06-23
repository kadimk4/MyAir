from django.contrib.auth import authenticate, login
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, request):
        username_ = request.data.get('username')
        password_ = request.data.get('password')

        user = authenticate(
            username=username_,
            password=password_
        )
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        login(request, user)
        return request.data
