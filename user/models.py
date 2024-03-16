from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from project.custom_Models import CustomModel


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields["is_active"] = True
        return super().create_superuser(username, email, password, **extra_fields)



class User(CustomModel, AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(null=True, blank=True)
    
    
    objects = CustomUserManager()
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email