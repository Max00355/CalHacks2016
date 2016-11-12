from flask import *
import webhook

app = Flask(__name__)

app.register_blueprint(webhook.app)

if __name__ == "__main__":
    app.run(debug=True)
