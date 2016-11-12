from twilio.rest import TwilioRestClient

ACCOUNT_SID = 'AC87769992cf0edbd7bfbd177e6c15a760'
AUTH_TOKEN = '5995687694981b0d7f5097a5ce418acb'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to = '2067084245',
    from_ = '2062072038',
    body = 'This is some text, bro!',
)
