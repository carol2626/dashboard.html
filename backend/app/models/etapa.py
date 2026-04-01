from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base

class Etapa(Base):
    __tablename__ = "etapas"

    id = Column(Integer, primary_key=True, index=True)
    # Campos Obrigatórios
    candidatura_id = Column(Integer, ForeignKey("candidaturas.id"), nullable=False)
    nome = Column(String, nullable=False)
    ordem = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    # Campos Opcionais
    descricao = Column(Text, nullable=True)
    data_prevista = Column(DateTime(timezone=True), nullable=True)
    data_conclusao = Column(DateTime(timezone=True), nullable=True)

    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # Cada etapa pertence a uma candidatura 
    candidatura = relationship("Candidatura", back_populates="etapas")
    # Uma etapa pode ter vários lembretes
    lembretes = relationship("Lembrete", back_populates="etapa")
