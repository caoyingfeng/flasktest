from sqlalchemy import create_engine,Column,Integer,String, \
    Float, Boolean,DECIMAL,Enum,DateTime,Text, func, and_, \
    or_,ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import enum
import random
from sqlalchemy.dialects.mysql import LONGTEXT


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '199232cyl'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class TagEnum(enum.Enum):
    python = "python"
    flask = "flask"
    django = "django"


class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User(username:%s)>"% self.username


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))
    author = relationship("User",backref="article")

    def __repr__(self):
        return "<Article(title:%s,content=%s)>" % (self.title,self.content)


Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username='cmx')
session.add(user)
session.commit()

article = Article(title='abc',content='123',uid=1)
session.add(article)
session.commit()

article = session.query(Article).first()
print(article.author)


