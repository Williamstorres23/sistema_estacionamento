from fastapi import FastAPI
from app.routes import user_routes  # Ajuste conforme a estrutura real

app = FastAPI()

# Adicionando rotas
app.include_router(user_routes.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Sistema de estacionamento rodando"}
