from referral.loggers.loggers import SmsLogger
import requests
import os
from dotenv import load_dotenv

load_dotenv()



def sent_sms(receptor: str, message: str):
    try:
        TOKEN = os.environ.get("SMS_TOKEN")
        TEMPLATE = 'otp'
        response = requests.get(
            f'http://api.kavenegar.com/v1/{TOKEN}/verify/lookup.json?receptor={receptor}&token={message}&template={TEMPLATE}')
        if response.status_code == 200:
            SmsLogger.info(f'message {message} sent to {receptor}')
        else:
            SmsLogger.warning(f'non 200 response, {response.text}')
        return response
    except Exception as error:
        SmsLogger.exception(f"API Exception occurred: {error}")
        return error


# a = sent_sms('09361243339', 'helloworld!')
# print(a)
