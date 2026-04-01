# vamos importar Session do SQLAlchemy - model Vaga - schema VagaCreate
from sqlalchemy.orm import Session
from app.models.vaga import Vaga
from app.schemas.vaga import VagaCreate

# cria objeto do model vaga com os dados recebidos 
# vaga é schema pydantic e db_vaga é objeto do SQLAlchemy
def create_vaga(db: Session, vaga: VagaCreate):
    db_vaga = Vaga(
        titulo=vaga.titulo,
        empresa=vaga.empresa,
        link=vaga.link,
        plataforma=vaga.plataforma,
        descricao=vaga.descricao,
        requisitos=vaga.requisitos,
        prazo_final=vaga.prazo_final,
        modalidade=vaga.modalidade,
        localizacao=vaga.localizacao,
        salario_bolsa=vaga.salario_bolsa,
        tipo_oportunidade=vaga.tipo_oportunidade
    )

    # marca vaga pra ser adicionada no banco (ainda nao salvou)
    db.add(db_vaga) 
    # agora sim salva no banco 
    db.commit()
    # atualiza o objeto db_vaga com os dados vindo do banco
    db.refresh(db_vaga)

    # devolve a vaga criada
    return db_vaga
