from fastapi import APIRouter

# serve pra organizar rotas em arquivos separados
router = APIRouter()

@router.get("/health") # rota de teste simples para verificar se API ta funcionando
def health_check():
    return {"message": "API funcionando corretamente! / Rota Health deu certo"}