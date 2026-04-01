from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.models.base import Base


class Candidatura(Base):
    __tablename__ = "candidaturas"

    id = Column(Integer, primary_key=True, index=True)
    # Campos Obrigatórios
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    vaga_id = Column(Integer, ForeignKey("vagas.id"), nullable=False)
    status_geral = Column(String, nullable=False)
    # Campos Opcionais
    data_candidatura = Column(DateTime(timezone=True), nullable=True)
    observacoes = Column(Text, nullable=True)
    data_ultima_atualizacao = Column(DateTime(timezone=True), nullable=True)
    prioridade = Column(String, nullable=True)

    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # Candidatura pertence a um usuario / uma vaga. pode ter varias etapas / varios lembretes 
    usuario = relationship("Usuario", back_populates="candidaturas")
    vaga = relationship("Vaga", back_populates="candidaturas")
    etapas = relationship("Etapa", back_populates="candidatura")
    lembretes = relationship("Lembrete", back_populates="candidatura")
