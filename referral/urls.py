from django.urls import path
from .views import SendReferralCode

urlpatterns = [
    path('send-referral/', SendReferralCode.as_view(), name='send_referral_code'),
]
