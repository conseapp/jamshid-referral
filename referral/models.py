from django.db import models
from datetime import timezone
import uuid


class Referral(models.Model):
    generated_date = models.DateTimeField(null=True, blank=True)
    inserted_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField(null=True, blank=True)
    code = models.CharField(max_length=8, editable=False, unique=True)
    # code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    active = models.BooleanField(default=True)

