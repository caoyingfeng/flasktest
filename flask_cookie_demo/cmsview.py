from flask import Blueprint,request

bp = Blueprint('cms', __name__,subdomain='cms')


@bp.route('/')
def index():
    username = request.cookies.get('username')
    return username or 'None'