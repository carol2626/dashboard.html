# centraliza a leitura das variaveis do projeto (URL do banco / chave JWT / MODO AMBIENTE)

# ele agora esta lendo o valor no .env que da mais segurança ao projeto
import os

#python, leita o arquivo .env e carregue as variaveis dele 
from dotenv import load_dotenv
load_dotenv()

# string de conexão com o banco.
DATABASE_URL = os.getenv("DATABASE_URL")