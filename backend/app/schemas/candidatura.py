from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel

# guarda os campos comuns (principais e nao obrigatorios)
class CandidaturaBase(BaseModel):
    usuario_id: int
    vaga_id: int
    status_geral: str # por enqt ainda aceita qlquer string 
    data_candidatura: Optional[date] = None
    observacoes: Optional[str] = None
    data_ultima_atualizacao: Optional[datetime] = None
    prioridade: Optional[str] = None

# Usado quando A candidatura vai ser criada.
class CandidaturaCreate(CandidaturaBase):
    pass

# Usado quando a API responde.
class CandidaturaResponse(CandidaturaBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True