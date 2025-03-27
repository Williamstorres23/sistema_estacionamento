from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.parking import Parking
from app.services.notification_service import enviar_email, enviar_sms

TEMPO_LIMITE = 3  # Tempo limite em horas

def verificar_permanencia_veiculos(db: Session):
    agora = datetime.utcnow()
    veiculos_em_risco = db.query(Parking).filter(
        (agora - Parking.hora_entrada) > timedelta(hours=TEMPO_LIMITE),
        Parking.hora_saida.is_(None)
    ).all()

    for veiculo in veiculos_em_risco:
        mensagem = f"Seu veículo ({veiculo.placa}) está no estacionamento há mais de {TEMPO_LIMITE} horas."
        enviar_email(veiculo.cliente.email, "Tempo Excedido!", mensagem)
        enviar_sms(veiculo.cliente.telefone, mensagem)
