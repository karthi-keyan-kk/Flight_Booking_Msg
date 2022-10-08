from twilio.rest import Client

TWILIO_SID = "ACfe7eceb760972be0a674bf8256226589"
TWILIO_AUTH_TOKEN = "daa0ebec61d63f387d34d7f2b0eafa7b"
TWILIO_VIRTUAL_NUMBER = "+12184004668"
TWILIO_VERIFIED_NUMBER = "+918056208161"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
