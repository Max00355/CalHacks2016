from flask import *
from utils import smartResponse, db
import pprint
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
