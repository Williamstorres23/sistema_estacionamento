from fastapi import APIRouter
from database.connection import SessionLocal
from app.models import Estacionamento

router = APIRouter()

# Simulação de vagas (deve ser ligado ao banco de dados real)
total_vagas = 20
vagas_ocupadas = [2, 5, 7, 10]  # Exemplo: Vagas que estão ocupadas

@router.get("/")
def obter_status_vagas():
    vagas_disponiveis = total_vagas - len(vagas_ocupadas)
    return {
        "total_vagas": total_vagas,
        "vagas_disponiveis": vagas_disponiveis,
        "vagas_ocupadas": len(vagas_ocupadas),
        "vagas_ocupadas_lista": vagas_ocupadas
    }
