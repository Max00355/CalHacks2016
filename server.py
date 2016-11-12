from flask import *

app = Blueprint(__name__, "server")

# =================================================
# Welcome
# =================================================
@app.route("/")
def welcome():

	# Get headers
	headers = request.headers
	print("headers:")
	print(headers)
	print("\n\n")

	# Get query string arguments
	query_args = request.args
	print("query_args:")
	print(query_args)
	print("\n\n")

	# Get form
	forms = request.form
	print("forms:")
	print(forms)
	print("\n\n")

	# JSON
	req_json = request.json
	print("forms:")
	print(forms)
	print("\n\n")

	# Print and return
	my_str = "I have received a message!"
	print(my_str)
	print("\n\n")



	return my_str

