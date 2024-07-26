from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
ROLE_CHOICE = [
    ('hotel', 'HOTEL'),
    ('user', 'USER'),
    ('admin', 'ADMIN'),
]

class User(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE_CHOICE, default='USER', max_length=100)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.id} - {self.username}"
