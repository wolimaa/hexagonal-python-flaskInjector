import connexion
from flask import request
from flask_restplus import Namespace, Resource, fields, Model
from flask_injector import inject
from core.domain.models.aso import Aso
from core.domain.services.iaso_sevice import IAsoService
from core.domain.services.iaso_funcionario_sevice import IAsoFuncionarioService
from injector import Module, Binder, singleton, Injector
from flask_sqlalchemy import SQLAlchemy

api = Namespace(
    'Aso', description='Operações referentes ao Atestado de Saúde Ocupacional')


todo = api.model('Todo', {
    'task': fields.String(required=True, description='The task details')
})


@api.route('/')
class AsoResource(Resource):
    @inject
    def __init__(self, aso_funcinario_service: IAsoFuncionarioService, aso_service: IAsoService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aso_service = aso_service
        self.aso_funcinario_service = aso_funcinario_service

    def home(self):
        pass
 
@api.route('/<string:oid>')
class AsoIdResource(Resource):
    @inject
    def __init__(self, aso_funcinario_service: IAsoFuncionarioService, aso_service: IAsoService, db: SQLAlchemy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aso_service = aso_service
        self.aso_funcinario_service = aso_funcinario_service
        self.db = db

    @api.doc(description='oid')
    def get(self, oid):
        '''Buscar ASO por oid'''
        return self.aso_service.get(oid)


