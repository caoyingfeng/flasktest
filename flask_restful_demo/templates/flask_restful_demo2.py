from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)

class Article(object):
    def __init__(self,title,content):
        self.title = title
        self.content = content

article = Article(title='xxx',content='xxx')


class ArticleView(Resource):
    resource_fields = {
        'title': fields.String,
        'content': fields.String
    }

    # @marshal_with(resource_fields)
    # def get(self):
    #     return {'title':'xxx'}
    @marshal_with(resource_fields)
    def get(self):
        return article

api.add_resource(ArticleView, '/article/',endpoint='article')


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)