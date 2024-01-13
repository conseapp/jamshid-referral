from .utils import check_authentication_api, code_generator
from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Referral
from .serializers import ReferralSerializer
import logging

logger = logging.getLogger(__name__)


class SendReferralCode(APIView):

    def get(self, request):
        return HttpResponseNotFound()

    def post(self, request, format=None):
        TOKEN = request.headers.get('token')
        if not TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # authentication_api = check_authentication_api(request, TOKEN)
        if True:
            referral = Referral.objects.filter(used=False).order_by('?').first()
            # referral = Referral.objects.create(code=code_generator().upper())
            serializer = ReferralSerializer(referral)
            logger.debug('Info message')

            return Response(serializer.data['code'], status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # check_authentication_api()

    # def post(self, request, format=None):
    #     TOKEN = request.headers.get('token')
    #     if not TOKEN:
    #         return Response(status=status.HTTP_403_FORBIDDEN)
    #     # authentication_api = check_authentication_api(request, TOKEN)
    #     if True:
    #         # referral = Referral.objects.filter(used=False).order_by('?').first()
    #         # print(str(referral.code))
    #         referral = Referral.objects.create(code=code_generator().upper())
    #         serializer = ReferralSerializer(referral)
    #
    #         return Response(serializer.data['code'], status=status.HTTP_202_ACCEPTED),  # serializer.data['code'],
    #     else:
    #         return Response(status=status.HTTP_401_UNAUTHORIZED)
