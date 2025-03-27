from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.alert_service import verificar_permanencia_veiculos
from app.services.parking_monitoring import verificar_vagas_disponiveis

router = APIRouter()

@router.get("/notificar-tempo/")
def notificar_tempo_excedido(db: Session = Depends(get_db)):
    verificar_permanencia_veiculos(db)
    return {"message": "Notificações enviadas para veículos com tempo excedido!"}

@router.get("/notificar-vagas/")
def notificar_vagas(db: Session = Depends(get_db)):
    total_vagas = 50  # Defina a capacidade total do estacionamento
    verificar_vagas_disponiveis(db, total_vagas)
    return {"message": "Notificações de vagas disponíveis enviadas!"}
