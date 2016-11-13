from flask import Response
import sendText

def purchaseHelp(to, resType):
    if resType == "card":
        xml = '<Response><Gather finishOnKey="*" action="https://44f611bc.ngrok.io/purchase?resType=exp"><Say>Please enter your credit card number and then press star.</Say></Gather></Response>'
        return Response(xml, mimetype='text/xml')
    elif resType == "exp":
        xml = '<Response><Gather finishOnKey="*" action="https://44f611bc.ngrok.io/purchase?resType=cvc"><Say>Please enter your credit card experation date and then press star.</Say></Gather></Response>'
        return Response(xml, mimetype='text/xml')
    elif resType == "cvc":
        xml = '<Response><Gather finishOnKey="*" action="https://44f611bc.ngrok.io/purchase?resType=finish"><Say>Please enter your credit card number and then press star.</Say></Gather></Response>'
        return Response(xml, mimetype='text/xml')
    elif resType == "finish":
        # WHAT DO WE DO WHEN THEY FINISH ENTERING EVERYHTING????
        xml = '<Response><Gather><Say>You have booked your flight. You should be getting a confimation code shortly.</Say></Gather></Response>'
        sendText.sendText(to, "Congratulations! You have booked your flight. Confirmation code: 086E7")
        return Response(xml, mimetype='text/xml')

    return Response("Please specify a response type - card, exp, cvc", mimetype='text/html')
    
