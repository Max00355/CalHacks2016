from flask import *
import server

app = Flask(__name__)

app.register_blueprint(server.app)

if __name__ == "__main__":
    app.run(debug=True)
