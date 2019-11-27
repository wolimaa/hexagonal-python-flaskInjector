from interface import implements
from core.domain.repositories.iaso_repository import IAsoRepository
from sqlalchemy import Integer, Column, create_engine, ForeignKey, engine


class AsoRepository(implements(IAsoRepository)):
    @inject
    def __init__(self, context: engine.Connection):

        def getAso(self, oid):
            result = context.execute("select username from users")
            context.close()
