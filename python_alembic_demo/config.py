HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_alembic_demo'
USERNAME = 'root'
PASSWORD = '199232cyl'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

