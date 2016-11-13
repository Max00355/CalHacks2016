
def purchaseHelp(resType)
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
        print("IT IS FINISHED")
        return("IT IS FINISHED!")

    return Response("Please specify a response type - card, exp, cvc", mimetype='text/html')
    