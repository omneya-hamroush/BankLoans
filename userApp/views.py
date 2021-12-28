from django.shortcuts import render
from userApp import models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token


class LoginView(TokenObtainPairView):
    pass


class LoginViewSet(ObtainAuthToken):
    """Checks login creds and returns auth token"""


    def post(self, request):

        user = models.User.objects.filter(email=request.data['username'])
        if user:
            user = user[0]

            user.save()
            is_correct_password = user.check_password(
                request.data['password'])
            if not user.is_active and is_correct_password:
                tokens = Token.objects.filter(user=user)
                tokens.delete()

                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "token": token.key,

                })

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']


        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'is_active': user.is_active,

        })
