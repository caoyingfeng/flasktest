from sqlalchemy import create_engine,Column,Integer,String, Float, Boolean,DECIMAL,Enum,DateTime,TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
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
    id = Column(Integer,primary_key=True,autoincrement=True)
    price = Column(Float)
    is_delete = Column(Boolean)
    total_price = Column(DECIMAL(10,4))
    tag = Column(Enum(TagEnum))
    create_time = Column(DateTime)
    title = Column(TEXT)
    content = Column(LONGTEXT)



Base.metadata.drop_all()
Base.metadata.create_all()
article = Article(price=19.9)
session.add(article)
session.commit()

from datetime import date
from datetime import datetime
from datetime import time
