from flask import Flask,session
from flask_session import Session
from redis import Redis

app = Flask(__name__)
# app.secret_key = "fegazgv"
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(host="127.0.0.1", port=6379, db=6)


Session(app)

@app.route("/")
def index():
    session['user'] = 'value'
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)