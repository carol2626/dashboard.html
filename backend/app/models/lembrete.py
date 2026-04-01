from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.models.base import Base


class Lembrete(Base):
    __tablename__ = "lembretes"

    id = Column(Integer, primary_key=True, index=True)
    # campos Obrigatorios
    candidatura_id = Column(Integer, ForeignKey("candidaturas.id"), nullable=False)
    titulo = Column(String, nullable=False)
    data_lembrete = Column(DateTime(timezone=True), nullable=False)
    status = Column(String, nullable=False)
    # Campos Opcionais
    etapa_id = Column(Integer, ForeignKey("etapas.id"), nullable=True)
    descricao = Column(Text, nullable=True)

    criado_em = Column(DateTime(timezone=True), server_default=func.now())