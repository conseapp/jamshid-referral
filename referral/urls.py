from django.urls import path
from .views import SendReferralCode
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('send-referral/', SendReferralCode.as_view(), name='send_referral_code'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
