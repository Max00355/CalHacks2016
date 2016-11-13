from twilio.rest import TwilioRestClient

ACCOUNT_SID = 'AC735604fda9d8b915edeecb9507965e37' #'AC87769992cf0edbd7bfbd177e6c15a760'
AUTH_TOKEN = 'bab3976396b77198d3cb80f99abb17c5' #'5995687694981b0d7f5097a5ce418acb'

def sendText(to, body):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to = to,
        from_ = '+12138066615', #'2062072038',
        body = "\n\n" + body,
    )
