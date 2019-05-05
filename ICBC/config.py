import os


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'icbc_demo'
USERNAME = 'root'
PASSWORD = '199232cyl'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
# TEMPLATES_AUTO_RELOAD = True