from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_type = models.CharField(default='visitor', choices=(('visitor', 'visitor'), ('author', 'author')))
