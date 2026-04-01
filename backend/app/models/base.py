# vai guardar a base comum do SQLAlchemy

# importando a função que cria a base dos models.
from sqlalchemy.orm import declarative_base

# criando a nossa base principal (estrutura que os models vao herdar)
Base = declarative_base()