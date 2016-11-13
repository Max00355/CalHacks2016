from flask import *
from utils import smartResponse, db
import pprint
from utils import purchaseHelp
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

@app.route("/purchase", methods=['POST'])
def purchase():
    resType = request.args.get('resType')
    digits = request.form.get('Digits')
    to = request.form.get('to')
    print(digits)

    # NEED TO STORE DIGITS?

    return(purchaseHelp.purchaseHelp(to, resType))
    
