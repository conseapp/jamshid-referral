from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Referral
from .serializers import ReferralSerializer


@receiver(post_save, sender=Referral)
def create_serializer(sender, instance, **kwargs):
    ReferralSerializer(instance)

