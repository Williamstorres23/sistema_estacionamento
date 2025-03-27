from sqlalchemy.orm import Session
from app.models.parking import Parking
from app.models.client import Client
from app.services.notification_service import enviar_email, enviar_sms

def verificar_vagas_disponiveis(db: Session, total_vagas: int):
    vagas_ocupadas = db.query(Parking).filter(Parking.hora_saida.is_(None)).count()
    vagas_disponiveis = total_vagas - vagas_ocupadas

    if vagas_disponiveis > 0:
        clientes = db.query(Client).all()
        for cliente in clientes:
            mensagem = f"Há {vagas_disponiveis} vagas disponíveis no estacionamento. Reserve agora!"
            enviar_email(cliente.email, "Vagas Disponíveis!", mensagem)
            enviar_sms(cliente.telefone, mensagem)
