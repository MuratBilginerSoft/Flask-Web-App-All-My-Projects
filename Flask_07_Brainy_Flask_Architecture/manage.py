from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import App, DB

migrate = Migrate(App, DB)
manager = Manager(App)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()