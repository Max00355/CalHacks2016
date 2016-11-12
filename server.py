from flask import Flask

app = Flask(__name__)

# =================================================
# Welcome
# =================================================
@app.route("/")
def welcome():
	my_str = "I have received a message!"
	print(my_str)
	return my_str

if __name__ == '__main__':
	app.run()