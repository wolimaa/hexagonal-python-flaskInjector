import os
import logging
from injector import Module, Binder, singleton, Injector, inject, provider
from flask import Flask
from flask_script import Manager
from flask_restplus import Api
from flask_environments import Environments
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.ext.declarative import declarative_base
from flask_injector import FlaskInjector
from presentation import config
from presentation.controllers import api
from presentation.controllers import app
from core.domain.services.iaso_funcionario_sevice import IAsoFuncionarioService
from core.application.services.aso_funcionario_sevice import AsoFuncionarioService
from core.domain.services.iaso_sevice import IAsoService
from core.application.services.aso_sevice import AsoService
from core.utils.injection_context import InjectionContext

env = Environments(app)
env.from_object(config)
Base = declarative_base()


class AppModule(Module):
    def __init__(self, app):
        self.app = app

    """Configure the application."""
    def configure(self, binder: Binder):
        db = self.configure_db(self.app)
    # migrate = Migrate(self.app, db)
        
        binder.bind(SQLAlchemy, to=db, scope=singleton)
        binder.bind(interface=IAsoFuncionarioService,
                    to=AsoFuncionarioService(), scope=singleton)
        binder.bind(interface=IAsoService, to=AsoService(), scope=singleton)
        binder.bind(Cache, to=Cache(app), scope=singleton)
        binder.bind(Api, to=api)
        

    def configure_db(self, app):
        db = SQLAlchemy(app)
        Base.metadata.create_all(db.engine)
        return db


def startup(params):
    app.config.from_object(params)
    logging.basicConfig(filename='logging.conf', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    injector = Injector([AppModule(app)])
    InjectionContext(injector);
    FlaskInjector(app=app, injector=injector)
    return app


app = startup(
    f'config.{os.getenv("FLASK_ENV")}' or 'config.Developement')
manager = Manager(app)
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
