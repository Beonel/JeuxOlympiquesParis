from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

