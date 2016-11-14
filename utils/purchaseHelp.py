from flask import Response
import sendText
import string
import random
from db import db

def purchaseHelp(to, resType):
    if resType == "card":
        xml = '<Response><Gather finishOnKey="#" action="http://rosterentryform.zapto.org/purchase?resType={}-exp"><Say>Please enter your credit card number and then press pound.</Say></Gather></Response>'.format(to)
        return Response(xml, mimetype='text/xml')
    elif resType == "exp":
        xml = '<Response><Gather finishOnKey="#" action="http://rosterentryform.zapto.org/purchase?resType={}-cvc"><Say>Please enter your credit card experation date and then press pound.</Say></Gather></Response>'.format(to)
        return Response(xml, mimetype='text/xml')
    elif resType == "cvc":
        xml = '<Response><Gather finishOnKey="#" action="http://rosterentryform.zapto.org/purchase?resType={}-finish"><Say>Please enter your credit card cvc number and then press pound.</Say></Gather></Response>'.format(to)
        return Response(xml, mimetype='text/xml')
    elif resType == "finish":
        # WHAT DO WE DO WHEN THEY FINISH ENTERING EVERYHTING????
        xml = '<Response><Gather><Say>Your flight has been booked. You will receive a text message containing your confirmation code shortly. Thank you.</Say></Gather></Response>'
        for f in db[to]['flightInfo'].split("--"):
            if "Number: {}".format(db[to]["selectedFlight"]) in f:
                break
        print to
        sendText.sendText(to, "Confirmed Flight Info\n{}\nYour confirmation code is: {}".format(f, ''.join([random.choice(string.uppercase + string.digits) for x in range(6)])))
        return Response(xml, mimetype='text/xml')

    return Response("Please specify a response type - card, exp, cvc", mimetype='text/html')
    
