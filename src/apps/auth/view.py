from django.contrib.auth import logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.auth.serializers import AuthSerializer


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthSerializer

    def post(self, request):
        # repository = Auth.create('auth')
        # response = repository.validate(request)
        a = AuthSerializer()
        response = a.validate(request)
        if response:
            return Response('cool', status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})
