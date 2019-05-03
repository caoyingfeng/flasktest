from flask import Flask,Response
from cmsview import bp


app = Flask(__name__)
app.register_blueprint(bp)
app.config["SERVER_NAME"]='hy.com:5000'


@app.route("/")
def hello():
    resp = Response('hello')
    resp.set_cookie('username','cmx',max_age=60*60*60, domain='.hy.com')
    return resp


if __name__ == '__main__':
    app.run(debug=True)