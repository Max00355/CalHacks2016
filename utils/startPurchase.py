from twilio.rest import TwilioRestClient

def startPurchase(to):
    to = to.replace("+", "")
    # Get these credentials from http://twilio.com/user/account
    account_sid = 'AC735604fda9d8b915edeecb9507965e37' #"AC87769992cf0edbd7bfbd177e6c15a760"
    auth_token = 'bab3976396b77198d3cb80f99abb17c5' #"5995687694981b0d7f5097a5ce418acb"
    client = TwilioRestClient(account_sid, auth_token)

    # Make the call
    call = client.calls.create(to=to,  # Any phone number
                               from_= "+12138066615", #"+12062072038", # Must be a valid Twilio number
                               url="http://44f611bc.ngrok.io/purchase?resType={}-card".format(to))
