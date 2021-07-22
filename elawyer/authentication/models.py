from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Create your models here.

class User(AbstractUser):
    username = models.CharField(_("Username"), unique=True, max_length=150, blank=True, null=True)
    email = models.EmailField(_("Email"), unique=True, max_length=255)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.get_full_name()
