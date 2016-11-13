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
    phone = data.get("to").replace("+", '')

    resp = smartResponse.smartResponse("getFlights", {
        "from":fromLocation,
        "to":toLocation,
        "date":date
    })
    db.db[phone] = {"flightInfo":resp, "cardInfo":[]}
    return resp

@app.route('/initpurchase', methods=['POST'])
def initpurchase():
    request.form = request.get_json()
    to = request.form.get('to').replace("+", "")
    flight = request.form.get("flightNum")
    db.db[to]['selectedFlight'] = flight
    startPurchase.startPurchase(to)
    return "You will receive a call in a few seconds prompting you to fill out your payment info."

@app.route("/purchase", methods=['POST'])
def purchase():
    resType = request.args.get('resType')
    to,resType = resType.split("-")
    digits = request.form.get('Digits')
    if "cardInfo" in db.db[to] and digits:
        db.db[to]["cardInfo"].append(digits)
    # NEED TO STORE DIGITS?
    return(purchaseHelp.purchaseHelp(to, resType))
    
