from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from user.models import User
from project.services import CustomModelSerializer


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=200)
    refresh_token = serializers.CharField(max_length=200)


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(
        trim_whitespace=False,
    )

    def validate(self, attrs):
        password = attrs.get("password", None)
        email = attrs.get("email")
        user = self._login_by_login_email(email, password)
        attrs["user"] = user
        return attrs

    def _login_by_login_email(self, email, password):
        user = User.objects.filter(email=email).first()
        if user is None:
            self._raise_login_validation_error()
        if user and not user.check_password(password):
            self._raise_login_validation_error()

        return user

    def _raise_login_validation_error(self):
        msg = {"details": [_("Unable to log in with provided credentials.")]}
        raise serializers.ValidationError(msg, code="authorization")


class UserSerializer(CustomModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "email",
            "first_name",
            "last_name",
            "username"
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate(self, validated_data):
        if self.context["request"].method == "POST":
            if "email" not in validated_data:
                raise ValidationError(_("you must provide email to signUp"))

            if User.objects.filter(
                email=validated_data["email"], is_active=True
            ).exists():
                raise serializers.ValidationError(_("Email already exist"))

        return validated_data
