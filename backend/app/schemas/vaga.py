# aqui usei date e date time pois existe campo prazo_final como data e criado_em data e hora
# date é so dia mes e ano / datetime é dia mes ano minuto hora segundo
from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel

# Guarda os campos comuns.
class VagaBase(BaseModel):
    titulo: str
    empresa: str
    link: Optional[str] = None
    plataforma: Optional[str] = None
    descricao: Optional[str] = None
    requisitos: Optional[str] = None
    prazo_final: Optional[date] = None
    modalidade: Optional[str] = None
    localizacao: Optional[str] = None
    salario_bolsa: Optional[str] = None
    tipo_oportunidade: Optional[str] = None

# Usado quando A vaga vai ser criada.
class VagaCreate(VagaBase):
    pass

# Usado quando a API responde.
class VagaResponse(VagaBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True