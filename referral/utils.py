from django.utils import timezone

from .models import Referral
import random
import string
import requests
import logging

logger = logging.getLogger(__name__)


def check_authentication_api(request, token):
    _, received_token = token.split()
    api_endpoint = 'https://api.mafia.jamshid.app/auth/check-token'
    headers = {'Authorization': f'Bearer {received_token}'}
    response = None
    try:
        response = requests.post(api_endpoint, headers=headers)
        response_json = response.json()
        if response_json["status"] == 200 or response_json["status"] == 201:
            return True
        elif response_json["status"] == 500:
            logger.warning("Unauthorized access to api.mafia.jamshid.app/auth/check-token")
            return False
    except Exception as err:
        logger.warning(err)
        # print(err)
        return False


def code_generator():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def referral_generator():
    code = code_generator()
    return Referral.objects.create(code=code, generated_date=timezone.now())
