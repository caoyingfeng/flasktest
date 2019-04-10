from flask import Flask,render_template,request
from wtforms.fields import simple, core
from wtforms import validators
from wtforms import Form

app = Flask(__name__)


class LoginForm(Form):
    username = simple.StringField(
        label="用户名", # 标签标记
        validators=[validators.DataRequired(message="用户名不能为空"),
                    validators.Length(min=3,max=8,message="长度不对")],
        description='', #  描述标记
        id=None, # 标签id
        default=None,
        widget=None, # 默认组件（input type='text'）
        render_kw=None, #{"class":"my_login"}
    )
    password = simple.PasswordField(
        label="密码",  # 标签标记
        validators=[validators.DataRequired(message="密码不能为空"),
                    validators.Length(min=3, max=16, message="密码长度不对")],
        description='',  # 描述标记
        id=None,  # 标签id
        default=None,
        widget=None,  # 默认组件（input type='text'）
        render_kw=None,  # {"class":"my_login"}
    )


class RegForm(Form):
    username = simple.StringField(
        label="用户名", # 标签标记
        validators=[validators.DataRequired(message="用户名不能为空"),
                    validators.Length(min=3,max=8,message="用户名长度不对")],
    )
    password = simple.PasswordField(
        label="密码",  # 标签标记
        validators=[validators.DataRequired(message="密码不能为空"),
                    validators.Length(min=3, max=16, message="密码长度不对")],
    )
    repassword = simple.PasswordField(
        label="确认密码",  # 标签标记
        validators=[validators.equal_to(fieldname="password", message="密码不一致")],
    )

    gender = core.RadioField(
        label="性别",
        coerce=int,
        choices={
            (1, "女"),
            (2, "男"),
        },
        default=1
    )

    hobby = core.SelectMultipleField(
        label="爱好",
        coerce=int,
        choices={
            (1, "琴"),
            (2, "棋"),
            (3, "书"),
            (4, "画"),
        },
        default=1
    )


@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == "GET":
        fm = LoginForm()
        return render_template("index.html", wtf=fm)
    else:
        new_fm = LoginForm(request.form)
        if new_fm.validate():
            return new_fm.data.get("username")
        else:
            return render_template('index.html', wtf=new_fm)


@app.route("/reg",methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        rf = RegForm()
        return render_template("reg.html", rf=rf)
    else:
        new_rf = RegForm(request.form)
        if new_rf.validate():
            return new_rf.data.get("username")
        else:
            return render_template('reg.html', rf=new_rf)


if __name__ == '__main__':
    app.run(debug=True)