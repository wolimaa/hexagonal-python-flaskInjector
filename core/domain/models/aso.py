# coding: utf-8
import datetime
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel

Base = declarative_base()


class Aso(Base):
    __tablename__ = 'aso'

    oid = Column(Integer, primary_key=True)
    altura = Column(String())
    anexo = Column(String())
    data = Column(DateTime())
    ehasoatual = Column(Boolean())
    faixaimc = Column(String())
    observacao = Column(String())
    peso = Column(String())
    tipo = Column(String())
    funcionario_oid = Column(Integer())
    statuspreenchimento = Column(String())
    tipoaso = Column(String())
    aptoinapto = Column(Boolean())
    candidato_oid = Column(String())
    resultado = Column(String())

    def __init__(self, oid, altura, anexo, data, ehasoatual, faixaimc, observacao, peso, tipo, funcionario_oid,
                 statuspreenchimento, tipoaso, aptoinapto, candidato_oid, resultado):
        self.oid = oid
        self.altura = altura
        self.anexo = anexo
        self.data = data
        self.ehasoatual = ehasoatual
        self.faixaimc = faixaimc
        self.observacao = observacao
        self.peso = peso
        self.tipo = tipo
        self.funcionario_oid = funcionario_oid
        self.statuspreenchimento = statuspreenchimento
        self.tipoaso = tipoaso
        self.aptoinapto = aptoinapto
        self.candidato_oid = candidato_oid
        self.resultado = resultado

    def __repr__(self):
        return '<id {}>'.format(self.oid)

    def serialize(self):
        return {
            'oid': self.oid,
            'aptoinapto': self.aptoinapto,
            'tipoaso': self.tipoaso,
            'resultado': self.resultado
        }
