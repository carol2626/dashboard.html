from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
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