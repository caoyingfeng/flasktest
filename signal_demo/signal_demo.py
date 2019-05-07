from flask import Flask,render_template, request, g, template_rendered
from signals import login_signal
from blinker import Namespace
app = Flask(__name__)


def template_rendered_func(sender, template,context):
    print('sender',sender)
    print('template', template)
    print('context', context)


template_rendered.connect(template_rendered_func)


@app.route('/')
def hello_world():
    # a = 1/0
    return render_template('index.html')


@app.route('/login/')
def login():
    username = request.args.get('username')
    if username:
        g.username = username
        login_signal.send()
        return '登陆成功'
    else:
        return '请输入用户名'


if __name__ == '__main__':
    app.run(debug=True)