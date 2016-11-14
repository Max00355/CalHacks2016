from twilio.rest import TwilioRestClient
from getKeys import keys

ACCOUNT_SID = keys['twilio']['public'] 
AUTH_TOKEN = keys['twilio']['private']

def sendText(to, body):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to = to,
        from_ = '+12138066615', #'2062072038',
        body = "\n\n" + body,
    )
