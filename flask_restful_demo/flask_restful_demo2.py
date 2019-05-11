from flask import Flask,blueprints
from flask_restful import Api, Resource, fields, marshal_with
from exts import db
import config
from models import User,Article, Tag
from articleview import article_bp


app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(article_bp)
db.init_app(app)
# api = Api(app)

# class Article(object):
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content
#
# article = Article(title='xxx',content='xxx')
#
#
# class ArticleView(Resource):
#     resource_fields = {
#         'title': fields.String,
#         'content': fields.String
#     }
#
#     # @marshal_with(resource_fields)
#     # def get(self):
#     #     return {'title':'xxx'}
#     @marshal_with(resource_fields)
#     def get(self):
#         return article
#
# api.add_resource(ArticleView, '/article/',endpoint='article')



@app.route('/')
def index():
    user = User(username='cmx',email='cmx@qq.com')
    article = Article(title='abc',content='123')
    article.author=user
    tag1 = Tag(name='c++')
    tag2 = Tag(name='python')
    article.tag.append(tag1)
    article.tag.append(tag2)
    db.session.add(article)
    db.session.commit()
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)