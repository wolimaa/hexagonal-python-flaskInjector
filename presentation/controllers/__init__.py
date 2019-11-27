from flask import Flask
from flask_restplus import Api
from presentation.controllers.aso_controller import api as ns1
from presentation.controllers.aso_funcionario_controller import api as ns2

app = Flask(__name__)
api = Api(app, version='1.0', title='SIV Saúde API',
          description='Restfull API Pilar Saúde')
# api.init_app(app)
api.add_namespace(ns1, path='/aso')
api.add_namespace(ns2, path='/asofuncionario')
