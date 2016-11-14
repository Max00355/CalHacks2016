from twilio.rest import TwilioRestClient
from getKeys import keys

def startPurchase(to):
    to = to.replace("+", "")
    # Get these credentials from http://twilio.com/user/account
    account_sid = keys['twilio']['public']
    auth_token =  keys['twilio']['private']
    client = TwilioRestClient(account_sid, auth_token)

    # Make the call
    call = client.calls.create(to=to,  # Any phone number
                               from_= "+12138066615", #"+12062072038", # Must be a valid Twilio number
                               url="http://rosterentryform.zapto.org/purchase?resType={}-card".format(to))
