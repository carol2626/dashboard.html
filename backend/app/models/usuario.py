from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.models.base import Base

# Criando classe usuario, que herda de base, SQLAlchemy entende que é model de banco
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    # Campos Obrigatorios
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    senha_hash = Column(String, nullable=False)
    curso = Column(String, nullable=False)
    # Campos Opcionais
    semestre = Column(Integer, nullable=True)
    nivel_ingles = Column(String, nullable=True)
    nivel_espanhol = Column(String, nullable=True)
    curriculo_link = Column(String, nullable=True)
    resumo_profissional = Column(Text, nullable=True)
    habilidades = Column(Text, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())