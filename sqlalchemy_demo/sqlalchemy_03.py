from sqlalchemy import create_engine,Column,Integer,String, Float, Boolean,DECIMAL,Enum,DateTime,TEXT, func
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

    def __repr__(self):
        return "<Article(title:%s)>" % self.title


Base.metadata.drop_all()
Base.metadata.create_all()

for x in range(6):
    article = Article(title='title%s'%x, price=random.randint(50,100))
    session.add(article)
session.commit()


# article = session.query(Article).all()
# print(article)

# articles = session.query(Article.title, Article.price).all()
# print(articles)

# result = session.query(func.count(Article.id)).all()
# print(result)
#
# result = session.query(func.avg(Article.price)).first()
# print(result)

# result = session.query(func.max(Article.price)).first()
# print(result)

# result = session.query(func.min(Article.price)).first()
# print(result)

# result = session.query(func.sum(Article.price)).first()
# print(result)

print(func.sum(Article.price))

