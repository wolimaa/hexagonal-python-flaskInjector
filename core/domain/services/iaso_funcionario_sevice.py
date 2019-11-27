from interface import implements, Interface


class IAsoFuncionarioService(Interface):
    def getAsoFuncionario(self, oid_funcionario):
        pass

    def getGHEFuncionarioPorAso(self, oid_funcionario, oid):
        pass
