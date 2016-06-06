import os
from shutil import rmtree
from flask.ext.script import Manager, Command
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy.exc import ProgrammingError
from app import app, db, init_db, drop_db

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class CreateDB(Command):
    """Creates the flaskr_tdd database"""

    def run(self):
        from app import init_db
        init_db()

manager.add_command('createdb', CreateDB())


class DropDB(Command):
    """Drops the flaskr_tdd database"""

    def run(self):
        from app import drop_db
        rmtree('migrations')
        try:
            drop_db()
        except ProgrammingError:
            print('ERROR: No flaskr_tdd database to delete')

manager.add_command('dropdb', DropDB())

if __name__ == '__main__':
    manager.run()
