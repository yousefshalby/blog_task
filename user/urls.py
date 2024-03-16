from django.urls import path

from user.views import (
    LoginView,
    LogoutView,
    UserView,
)

from dj_rest_auth.jwt_auth import get_refresh_view




urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("signup", UserView.as_view(), name="signup"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view()),

]