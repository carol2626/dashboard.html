# Cria a conexão com o banco (postgresql) usando os dados que vieram do config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# usa o valor lido pelo config.py para criar a conexão
from app.core.config import DATABASE_URL

# engine é o objeto que conversa com o banco (conexão principal)
engine = create_engine(DATABASE_URL)

# sessionmaker cria sessões para trabalhar com o banco 
# sessionlocal são sessões para conversar com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# função para abrir uma sessão com o banco / usar a sessão e fecha-la
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

