from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.vaga import create_vaga
from app.db.database import get_db
from app.schemas.vaga import VagaCreate, VagaResponse

# criando grupo de rotas de vagas
# prefix significa que todas as rotas começaram com /vagas
router = APIRouter(prefix="/vagas", tags=["Vagas"])

# define que a função responde a requisição post 
@router.post("/", response_model=VagaResponse)
def criar_vaga(vaga: VagaCreate, db: Session = Depends(get_db)):
    return create_vaga(db=db, vaga=vaga)