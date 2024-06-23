from django.contrib.auth import logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.auth.serializers import AuthSerializer
from utils.factories.service_factory import ServiceFactory


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthSerializer

    def post(self, request):
        serializer = ServiceFactory.create('auth')
        response = serializer.validate(request)
        if response:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
