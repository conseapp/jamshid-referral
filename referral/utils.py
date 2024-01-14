from django.utils import timezone
from referral.loggers.loggers import AuthenticationApiLogger
from .models import Referral
import random
import string
import requests


def check_authentication_api(request, token):
    _, received_token = token.split()
    api_endpoint = 'https://api.mafia.jamshid.app/auth/check-token'
    headers = {'Authorization': f'Bearer {received_token}'}
    response = None
    try:
        response = requests.post(api_endpoint, headers=headers)
        response_json = response.json()
        if response_json["status"] == 200 or response_json["status"] == 201:
            AuthenticationApiLogger.info(f'successfully authenticated request for user {request.headers.get("user")}')
            return True
        elif response_json["status"] == 500:
            AuthenticationApiLogger.warning(
                'Unauthorized access to api.mafia.jamshid.app/auth/check-token for user {request.headers.get("user")}')
            return False
    except Exception as err:
        AuthenticationApiLogger.exception(f"Exception occurred: {err}")
        return False


def code_generator():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def referral_generator():
    code = code_generator()
    return Referral.objects.create(code=code, generated_date=timezone.now())
