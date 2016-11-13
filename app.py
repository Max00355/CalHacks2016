from flask import *
import webhook

app = Flask(__name__)
app.secret_key = "1939asdl12l3ksdjfkdfgo32l423"

app.register_blueprint(webhook.app)

if __name__ == "__main__":
    app.run(debug=True, port=8002, host="0.0.0.0")
