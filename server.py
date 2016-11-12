from flask import *

app = Blueprint(__name__, "server")

# =================================================
# Welcome
# =================================================
@app.route("/")
def welcome():
	my_str = "I have received a message!"
	print(my_str)
	return my_str

