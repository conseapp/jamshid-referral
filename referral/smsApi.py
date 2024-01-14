from referral.loggers.loggers import SmsLogger
import requests


def sent_sms(receptor: str, message: str):
    try:
        TOKEN = '4E4E7566354D53344544343456785A6F5562452F69506E4A6E4A63636E62354D6242664A4846374F6958383D'
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
