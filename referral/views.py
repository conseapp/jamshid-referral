from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Referral
from .serializers import ReferralSerializer


async def check_authentication_api(token, phone_number):
    api_endpoint = 'https://api.mafia.jamshid.app/auth/check-token'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(api_endpoint, headers=headers)
    response_json = response.json()
    if response_json["status"] == 200 or response_json["status"] == 201:
        return True
    elif response_json["status"] == 500:
        return False


class SendReferralCode(APIView):
    def post(self, request, format=None):
        referral = Referral.objects.create()
        headers = request.META
        print(headers)
        serializer = ReferralSerializer(referral)

        # check_authentication_api()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

