from core.domain.models import aso_funcionario
from core.domain.services.iaso_funcionario_sevice import IAsoFuncionarioService
from interface import implements, Interface


class AsoFuncionarioService(implements(IAsoFuncionarioService)):
    
    def getAsoFuncionario(self, oid_funcionario):
        return aso_funcionario(123)

    def getGHEFuncionarioPorAso(self, oid_funcionario, oid):
        return aso_funcionario(123)
