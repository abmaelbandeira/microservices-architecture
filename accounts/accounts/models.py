import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class UserUnderProtection(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    name = models.CharField(max_length=100)
    token = models.CharField(max_length=100, null=True)
    token_expiration_date = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.name
