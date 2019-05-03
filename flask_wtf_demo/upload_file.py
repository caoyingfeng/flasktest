from flask import Flask, request,render_template
# from wtforms import Form
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
from form import UploadForm
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')

@app.route('/')
def hello():
    return 'hello'


@app.route('/upload/',methods=['GET','POST'])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    else:
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            desc = request.form.get('desc')
            avatar = request.files.get('avatar')
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH,filename))
            print(desc)
            return '文件上传成功'
        else:
            print(form.errors)
            return 'fail'


@app.route('/images/<filename>/')
def get_image(filename):
    return send_from_directory(UPLOAD_PATH,filename)


if __name__ == '__main__':
    app.run(debug=True)