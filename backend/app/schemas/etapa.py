from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class EtapaBase(BaseModel):
    candidatura_id: int
    nome: str
    ordem: int
    status: str
    descricao: Optional[str] = None
    data_prevista: Optional[date] = None
    data_conclusao: Optional[date] = None


class EtapaCreate(EtapaBase):
    pass


class EtapaResponse(EtapaBase):
    id: int
    criado_em: datetime

    # permite a conversão de objetos SQLAlchemy em resposta da API
    class Config:
        from_attributes = True