from flask import *

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

	print from_ , message
        return "ASD"
