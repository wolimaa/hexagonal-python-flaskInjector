import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_OPERATION_ID = True
    SWAGGER_UI_REQUEST_DURATION = True

    # Flask-Restplus 
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False


class Developement(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or  \
        'postgres://postgres:0000@localhost:5432/siv'


class Testing(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
        'postgres://postgres:0000@localhost:5432/siv'


class Production(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or  \
        'postgres://postgres:0000@localhost:5432/siv'
