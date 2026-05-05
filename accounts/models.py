import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta


class MagicLinkToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def is_valid(self):
        return not self.used and timezone.now() < self.created_at + timedelta(minutes=15)

    def __str__(self):
        return f'{self.email} — {self.token}'
