from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class LembreteBase(BaseModel):
    candidatura_id: int
    etapa_id: Optional[int] = None
    titulo: str
    data_lembrete: date
    status: str
    descricao: Optional[str] = None


class LembreteCreate(LembreteBase):
    pass


class LembreteResponse(LembreteBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True