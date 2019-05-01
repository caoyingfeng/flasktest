from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = '199232cyl'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<username: %s>"% self.username


class Article(db.Model):
    # __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref='articles')


db.drop_all()
db.create_all()

# user = User(username='cmx')
# article = Article(title='title 1')
# article.author = user
# db.session.add(article)
# db.session.commit()

# db.session.query()
# order_by
# filter
# filter_by
# group_by
# join
# users = User.query.order_by(User.id.desc()).all()
# print(users)

# user = User.query.filter(User.username=='cmx').first()
# user.username = 'cmx1'
# db.session.commit()

# user = User.query.filter(User.username=='cmx1').first()
# db.session.delete(user)
# db.session.commit()


@app.route("/")
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)