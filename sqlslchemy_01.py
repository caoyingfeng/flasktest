from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '199232cyl'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

# conn = engine.connect()
# result = conn.execute('select 1')
# print(result.fetchone())

Base = declarative_base(engine)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)


Base.metadata.create_all()