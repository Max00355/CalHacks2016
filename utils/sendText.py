from twilio.rest import TwilioRestClient

ACCOUNT_SID = 'AC87769992cf0edbd7bfbd177e6c15a760'
AUTH_TOKEN = '5995687694981b0d7f5097a5ce418acb'

def sendText(to, body):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to = to,
        from_ = '2062072038',
        body = "\n\n" + body,
    )
