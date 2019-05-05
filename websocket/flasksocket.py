from flask import Flask, render_template, request
from gevent.pywsgi import  WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket
import json

app = Flask(__name__)

user_socket_list = []
user_socket_dict = {}

@app.route("/ws/<username>")
def ws(username):
    # print(request.environ)
    user_socket = request.environ.get("wsgi.websocket") #type:WebSocket
    if user_socket:
        # user_socket_list.append(user_socket)
        user_socket_dict[username] = user_socket
    # print(user_socket_list)
    print(len(user_socket_dict), user_socket_dict)
    while 1:
        msg = user_socket.receive()
        msg_dict = json.loads(msg)
        msg_dict["from_user"] = username
        to_user = msg_dict.get("to_user")
        u_socket = user_socket_dict.get(to_user) # type:WebSocket
        u_socket.send(json.dumps(msg_dict))
    #     for u_socket in user_socket_list:
    #         if user_socket == u_socket:
    #             continue
    #         try:
    #             u_socket.send(msg)
    #         except:
    #             continue
    # return "123"


@app.route("/")
def index():
    return render_template("ws.html")

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9527),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()