from sqlalchemy import create_engine,Column,Integer,String, Float, Boolean,DECIMAL,Enum,DateTime,Text, func, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50),nullable=False)
    price = Column(Float, nullable=False)
    content = Column(Text)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()

# session.query(Article).filter(Article.id == 1)

# article = session.query(Article).filter(Article.title == "title1").first()
# print(article)

# articles = session.query(Article).filter(Article.title != 'title0').all()
# print(articles)

articles = session.query(Article).filter(Article.title.like('title%')).all()
print(articles)


# for xxx in xxx
# def _in()
# articles = session.query(Article).filter(Article.title.in_(['title1','title2'])).all()
# print(articles)

# not in
# articles = session.query(Article).filter(~Article.title.in_(['title1','title2'])).all()
# print(articles)
# articles = session.query(Article).filter(Article.title.notin_(['title1','title2'])).all()
# print(articles)

# is null
# articles = session.query(Article).filter(Article.content==None).all()
# print(articles)

# is not null
# articles = session.query(Article).filter(Article.content!=None).all()
# print(articles)

# and
# articles = session.query(Article).filter(Article.title=='abc',Article.content=='abc').all()
# print(articles)

articles = session.query(Article).filter(or_(Article.title=='abc',Article.content=='abc'))
print(articles)