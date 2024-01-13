from kavenegar import KavenegarAPI, APIException, HTTPException
from loggers.loggers import SmsLogger


def sent_sms(receptor: str, message: str):
    try:
        api = KavenegarAPI(r'4E4E7566354D53344544343456785A6F5562452F69506E4A6E4A63636E62354D6242664A4846374F6958383D')
        params = {
            'sender': '10007119',
            'receptor': receptor,
            'template': 'otp',
            'message': message
        }
        # response = api.sms_send(params)
        response = 'hi'
        SmsLogger.info(f'message {message} sent to {receptor}')
        return response
    except APIException as e:
        error = ' '.join([arg.decode('utf-8') for arg in e.args])
        SmsLogger.exception(f"API Exception occurred: {error}")
        return None
    except HTTPException as e:
        error = ' '.join([arg.decode('utf-8') for arg in e.args])
        SmsLogger.exception(f"HTTP Exception occurred: {error}")
        return None


a = sent_sms('09361243339', '<hello, world!>')
print(a)
