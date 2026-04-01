from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, index=True)
    # Campos Obrigatório
    titulo = Column(String, nullable=False)
    empresa = Column(String, nullable=False)
    # Campos Opcionais
    link = Column(String, nullable=True)
    plataforma = Column(String, nullable=True)
    descricao = Column(Text, nullable=True)
    requisitos = Column(Text, nullable=True)
    prazo_final = Column(DateTime(timezone=True), nullable=True)
    modalidade = Column(String, nullable=True)
    localizacao = Column(String, nullable=True)
    salario_bolsa = Column(String, nullable=True)
    tipo_oportunidade = Column(String, nullable=True)

    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # uma vaga pode ter várias candidaturas
    candidaturas = relationship("Candidatura", back_populates="vaga")