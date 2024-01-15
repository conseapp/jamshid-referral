from .utils import check_authentication_api
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Referral
from .serializers import ReferralSerializer
from .smsApi import sent_sms
import re


class SendReferralCode(APIView):

    def get(self, request):
        return HttpResponseNotFound()

    def post(self, request, format=None):
        TOKEN = request.headers.get('token')
        USER = request.headers.get('user')
        pattern = r'^[B,b]earer\s([a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+)$'
        if not TOKEN or not USER:
            return Response(status=status.HTTP_403_FORBIDDEN)
        elif not re.match(pattern, TOKEN):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        authentication_api = check_authentication_api(request, TOKEN)
        if authentication_api:
            referral = Referral.objects.filter(used=False).order_by('?').first()
            # referral = Referral.objects.create(code=code_generator().upper())
            serializer = ReferralSerializer(referral)
            result = sent_sms(USER, serializer.data['code'])
            if result:
                referral.used = True
                referral.sent_to = USER
                referral.save()
                return Response(f'message sent to {USER}', status=status.HTTP_200_OK)
            else:
                return Response('failed to sent message', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
