# coding: utf-8
import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table, Text, text
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship
from core.domain.models.base_model import BaseModel


class AsoFuncionario(BaseModel):
    __tablename__ = 'asofuncionario'

    oid = Column(String())
    funcionario_oid = Column(String())
    dataultimanotificacaoasospendentes = Column(String())
    dataultimanotificacaoasosvencidos = Column(String())
    dataultimanotificacaoasoavencer = Column(String())
    dataultimanotificacaoconsolidadosupervisor = Column(String())
    statusasoexame = Column(String())
    tipomedico = Column(String())
    medico_oid = Column(String())
    medicoexterno_oid = Column(String())
    servicosauderesponsavelaso_oid = Column(String())
    usuariocriador_oid = Column(String())
    responsavelpcmso_oid = Column(String())
    datavencimentoaso = Column(String())
    ghe_oid = Column(String())
    ignorarmonitoramento = Column(String())
    asoretroativo = Column(String())
    
    def __init__(self, oid, funcionario_oid, dataultimanotificacaoasospendentes, dataultimanotificacaoasosvencidos, dataultimanotificacaoasoavencer,
                 dataultimanotificacaoconsolidadosupervisor, statusasoexame, tipomedico, medico_oid, medicoexterno_oid, servicosauderesponsavelaso_oid, usuariocriador_oid,
                 responsavelpcmso_oid, datavencimentoaso, ghe_oid, ignorarmonitoramento, asoretroativo):
        self.oid = oid
        self.funcionario_oid = funcionario_oid
        self.dataultimanotificacaoasospendentes = dataultimanotificacaoasospendentes
        self.dataultimanotificacaoasosvencidos = dataultimanotificacaoasosvencidos
        self.dataultimanotificacaoasoavencer = dataultimanotificacaoasoavencer
        self.dataultimanotificacaoconsolidadosupervisor = dataultimanotificacaoconsolidadosupervisor
        self.statusasoexame = statusasoexame
        self.tipomedico = tipomedico
        self.medico_oid = medico_oid
        self.medicoexterno_oid = medicoexterno_oid
        self.servicosauderesponsavelaso_oid = servicosauderesponsavelaso_oid
        self.usuariocriador_oid = usuariocriador_oid
        self.responsavelpcmso_oid = responsavelpcmso_oid
        self.datavencimentoaso = datavencimentoaso
        self.ghe_oid = ghe_oid
        self.ignorarmonitoramento = ignorarmonitoramento
        self.asoretroativo = asoretroativo

    def __repr__(self):
        return '<id {}>'.format(self.oid)

    def serialize(self):
        return {
            'oid': self.oid,
            'aptoinapto': self.aptoinapto,
            'tipoaso': self.tipoaso,
            'resultado': self.resultado
        }
