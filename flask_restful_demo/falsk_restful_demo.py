from flask import Flask,url_for
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class LoginView(Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username',type=str,help='用户名错误')
        parse.add_argument('password', type=str, help='用户名错误')
        args = parse.parse_args()
        print(args)
        return {'username': 'cmx'}


api.add_resource(LoginView,'/login/',endpoint='login')
# api.add_resource(LoginView,'/login/')


@app.route('/')
def index():
    print(url_for('login'))
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
