from flask import Flask,session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)


@app.route('/')
def index():
    session['username'] = '123'
    session.permanent = True
    return 'Hello'


@app.route('/get_session/')
def get_session():
    username = session.get('username')
    return username or 'no session'


@app.route('/delete_session/')
def delete_session():
    session.pop('username')
    # session.clear()
    return 'session删除'

if __name__ == '__main__':
    app.run(debug=True)