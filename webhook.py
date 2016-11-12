from flask import *
from utils import smartResponse

app = Blueprint(__name__, "server")

# =================================================
# Welcome
# =================================================
@app.route("/incoming", methods=['POST'])
def getText():
	
	# Get form
	forms = request.form    
    from_ = forms['From']
    message = forms['Body']

    # Send out smart response
    smartResponse.smartResponse(from_, message)

    # Return
	print from_ , message
    return "ASD"