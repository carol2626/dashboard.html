from fastapi import FastAPI
from app.routes.health import router as health_router

# criei a aplicação
app = FastAPI()

# conecta a rota criada no health.py com a aplicação principal
app.include_router(health_router)

# criei uma rota get
@app.get("/")
#define o que acontece quando alguém acessa a rota principal
def read_root():
    return {"message": "Backend Descomplica Vagas funcionando!"}