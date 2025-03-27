from sqlalchemy.orm import Session
from datetime import datetime
from app.models.payment import Payment
from app.models.parking import Parking

# Tarifas do estacionamento
TARIFA_POR_HORA = 5.00  

def calcular_valor(entrada: datetime, saida: datetime):
    tempo_total = (saida - entrada).total_seconds() / 3600  # Converte para horas
    return round(tempo_total * TARIFA_POR_HORA, 2)

def processar_pagamento(db: Session, estacionamento_id: int, metodo_pagamento: str):
    estacionamento = db.query(Parking).filter(Parking.id == estacionamento_id).first()
    if not estacionamento or not estacionamento.hora_saida:
        return {"error": "Estacionamento não encontrado ou veículo ainda não saiu"}

    valor = calcular_valor(estacionamento.hora_entrada, estacionamento.hora_saida)
    
    pagamento = Payment(
        estacionamento_id=estacionamento_id,
        valor=valor,
        metodo_pagamento=metodo_pagamento,
        status="Pago"
    )

    db.add(pagamento)
    db.commit()
    db.refresh(pagamento)

    return {"message": "Pagamento realizado com sucesso!", "valor_pago": valor}
