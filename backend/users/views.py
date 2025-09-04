from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserSignupSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response

class SignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

class CustomAuthToken(ObtainAuthToken):
    # Esto le dice a DRF que use también el BrowsableAPIRenderer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        # validamos credenciales
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)

        # obtenemos al usuario
        user = serializer.validated_data['user']
        # creamos o recuperamos el token
        token, _ = Token.objects.get_or_create(user=user)

        # devolvemos JSON (y además Browserable API nos pintará el form)
        return Response({'token': token.key})