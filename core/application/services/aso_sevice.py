from core.domain.models import aso
from core.domain.services.iaso_sevice import IAsoService
from core.domain.services.iaso_funcionario_sevice import IAsoFuncionarioService
from interface import implements, Interface
from flask_injector import inject
from injector import Module, Binder, singleton, Injector, inject
from flask_sqlalchemy import SQLAlchemy
from core.utils.injection_context import InjectionContext



class AsoService(implements(IAsoService)):
    # def __init__(self, db: SQLAlchemy):
    #   self.db = db
        # super().__init__(*args, **kwargs)
        # self.aso_service = aso_service
        # self.aso_funcinario_service = aso_funcionario_service
        # self.db = db
    def get(self, oid):
        inject = InjectionContext.inject.get()
        service = inject.get(self, interface=IAsoService, scope=singleton)
        # return 'teste de consulta de dados ao serviço. Id:' + oid
        return service.getAsoFuncionario(oid)

    def update(self, oid, aso):
        return ''
