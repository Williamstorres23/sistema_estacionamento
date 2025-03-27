from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.payment_service import processar_pagamento

router = APIRouter()

@router.post("/pagar/")
def pagar_estacionamento(estacionamento_id: int, metodo_pagamento: str, db: Session = Depends(get_db)):
    return processar_pagamento(db, estacionamento_id, metodo_pagamento)
