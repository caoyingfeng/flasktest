from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful_demo2 import app
from exts import db
import models


manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()