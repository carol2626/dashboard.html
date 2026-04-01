# para campos de data e hora como o criado_em
from datetime import datetime
# campo pode ser preenchido ou pode ser None
from typing import Optional
# base dos schemas do pydantic e emailstr é pra validar que o email parece um email
from pydantic import BaseModel, EmailStr

# Guarda os campos comuns.
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    curso: str
    semestre: Optional[int] = None
    nivel_ingles: Optional[str] = None
    nivel_espanhol: Optional[str] = None
    curriculo_link: Optional[str] = None
    resumo_profissional: Optional[str] = None
    habilidades: Optional[str] = None

# Usado quando o usuário vai ser criado.
class UsuarioCreate(UsuarioBase):
    senha: str

# Usado quando a API responde.
class UsuarioResponse(UsuarioBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True