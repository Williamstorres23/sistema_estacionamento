from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database.connection import Base
import datetime

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    estacionamento_id = Column(Integer, ForeignKey("parking.id"), nullable=False)
    valor = Column(Float, nullable=False)
    metodo_pagamento = Column(String, nullable=False)
    status = Column(String, default="Pendente")  # Pendente, Pago, Cancelado
    data_pagamento = Column(DateTime, default=datetime.datetime.utcnow)

    estacionamento = relationship("Parking", back_populates="pagamento")
