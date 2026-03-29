# Cria a conexão com o banco usando os dados que vieram do config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# usa o valor lido pelo config.py para criar a conexão
from app.core.config import DATABASE_URL

# engine é o objeto que conversa com o banco
engine = create_engine(DATABASE_URL) # cria base da conexão com o banco

# sessionmaker cria sessões para trabalhar com o banco 
# sessionlocal é o molde das sessões do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# função para abrir uma sessão com o banco / usar a sessão e fecha-la
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()