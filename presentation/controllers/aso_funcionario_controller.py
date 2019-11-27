from flask_restplus import Namespace, Resource, fields
import connexion
api = Namespace(
    'asosfuncionario', description='Operações referentes ao Atestado de Saúde Ocupacional do Funcionario')

aso = api.model('AsoFuncionario', {
    'oid': fields.String(required=True, description='Id do Aso'),
    'nome-funcionario': fields.String(required=True, description='Nome do funcionario')
})


ASOS = [
    {'oid': '1321321313', 'nome': 'Xonin'},
]


@api.route('/')
class AsoList(Resource):
    @api.doc('list_aso')
    @api.marshal_list_with(aso)
    def get(self):
        '''Lista dos top 10 asos - EXEMPLO'''
        return ASOS


