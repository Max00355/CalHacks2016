from flask import *
from utils import smartResponse, db
import pprint
from utils import purchaseHelp, startPurchase
app = Blueprint(__name__, "server")

# =================================================
# Welcome
# =================================================
@app.route("/getFlights", methods=['POST'])
def getText():
    data = request.get_json(silent=True)
    fromLocation = data.get("fromLoc")
    toLocation = data.get("toLoc")
    date = data.get("date")

    return smartResponse.smartResponse("getFlights", {
        "from":fromLocation,
        "to":toLocation,
        "date":date
    })

@app.route('/initpurchase', methods=['POST'])
def initpurchase():
    request.form = request.get_json()
    to = request.form.get('to')
    startPurchase.startPurchase(to)
    return "You will receive a call in a few seconds prompting you to fill out your payment info."

@app.route("/purchase", methods=['POST'])
def purchase():
    resType = request.args.get('resType')
    digits = request.form.get('Digits')
    to = request.form.get('to')
    if resType == "card":
        db.db[to] = {"card":digits}
    elif resType == "exp":
        db.db[to]["exp"] = digits
    elif resType == "cvc":
        db.db[to]["cvc"] = digits
    # NEED TO STORE DIGITS?

    return(purchaseHelp.purchaseHelp(to, resType))
    
