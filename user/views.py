from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from user.models import User
from rest_framework.generics import GenericAPIView
from user.serializers import (
    CustomAuthTokenSerializer,   
    TokenSerializer,
    UserSerializer,
)
from rest_framework.views import APIView
from rest_framework import status

class UserView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_authenticators(self):
        return [] if self.request.method == "POST" else super().get_authenticators()

    def get_object(self):
        return self.request.user

    def post(self, request):
        User.objects.filter(email=request.data["email"], is_active=False).delete()
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        user.is_app_user = True
        user.save()
        refersh_token = RefreshToken.for_user(user)
        access_token = refersh_token.access_token
        token_serializer = TokenSerializer(
            data={
                "refresh_token": str(refersh_token),
                "access_token": str(access_token),
            }
        )
        serializer.is_valid()
        token_serializer.is_valid()
        return Response(
            {
                "user": serializer.data,
                "token": token_serializer.data,
            },
            status=201,
        )


class LoginView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def _get_user(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data["user"]

    def post(self, request, *args, **kwargs):
        user = self._get_user(request)
        refersh_token = RefreshToken.for_user(user)
        access_token = refersh_token.access_token
        token_serializer = TokenSerializer(
            data={
                "refresh_token": str(refersh_token),
                "access_token": str(access_token),
            }
        )
        token_serializer.is_valid()

        return Response(
            {
                "token": token_serializer.data,
                "user": UserSerializer(user).data,
            }
        )


class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)