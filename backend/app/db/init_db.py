#init db = arquivo para inicializar o banco (executou a criação da tabela)

from app.db.database import engine
from app.models.base import Base
from app.models import Usuario, Vaga, Candidatura, Etapa, Lembrete

# essa linha olha todos os models que herdam de Base, le os metadados
# e cria a tabela no postgreSQL, caso nao existam 
def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tabelas criadas com sucesso!")