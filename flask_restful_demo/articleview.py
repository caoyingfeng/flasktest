from flask import Blueprint,render_template,make_response
from flask_restful import Resource,fields,marshal_with,Api
from models import User,Article,Tag

article_bp = Blueprint('article', __name__, url_prefix='/article')
api = Api(article_bp)


@api.representation('text/html')
def output_html(data,code,headers):
    resp = make_response(data)
    return resp


class ArticleView(Resource):

    resouce_fields={
        'article_title': fields.String(attribute='title'),
        'content': fields.String,
        'author': fields.Nested({
            'username': fields.String,
            'email': fields.String
        }),
        'tag': fields.List(fields.Nested({
            'id': fields.Integer,
            'name': fields.String
        }))
    }

    @marshal_with(resouce_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article


class ListView(Resource):

    def get(self):
        return render_template('list.html')


api.add_resource(ListView,'/list',endpoint='list')
api.add_resource(ArticleView,'/article/<article_id>',endpoint='article')
