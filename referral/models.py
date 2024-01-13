from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html

import uuid


class Referral(models.Model):
    generated_date = models.DateTimeField()
    inserted_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=8, editable=False, unique=True)
    # code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    used = models.BooleanField(default=False)

    def get_expired_date(self):
        if self.generated_date:
            return self.generated_date + timezone.timedelta(days=7)
        else:
            return self.inserted_date + timezone.timedelta(days=7)

    @admin.display
    def expired_date(self):
        return format_html('<span>{}</span>', self.get_expired_date())
