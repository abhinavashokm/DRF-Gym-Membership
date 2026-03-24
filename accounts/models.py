from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Role_Choices = (("user", "User"), ("owner", "Gym Owner"))
    role = models.CharField(max_length=10, choices=Role_Choices)
