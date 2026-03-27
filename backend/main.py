from fastapi import FastAPI

# criei a aplicação
app = FastAPI()

# criei uma rota 
@app.get("/")

#define o que acontece quando alguém acessa a rota principal
def read_root():
    return {"message": "Backend do Descomplica Vagas funcionando!"}