from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
session = sessionmaker(engine)()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)


Base.metadata.drop_all()
Base.metadata.create_all()


def add_data():
    p1 = Person(name='1',age=2)
    p2 = Person(name='2', age=3)
    session.add_all([p1,p2])
    session.commit()


def search_data():
    all_person = session.query(Person).all()
    # for p in all_person:
    #     print(p.name,p.age)
    # all_person = session.query(Person).filter_by(name='1').all()
    # all_person = session.query(Person).filter(Person.name=='1').all()
    for p in all_person:
        print(p.name,p.age)


def update_data():
    person = session.query(Person).filter(Person.name=='1').update({'name':'cy'})
    session.commit()
    print(person)


def delete_data():
    person = session.query(Person).filter(Person.name=='2').first()
    session.delete(person)
    session.commit()


if __name__ == '__main__':
    add_data()
    update_data()
    delete_data()
    search_data()
    session.close()

