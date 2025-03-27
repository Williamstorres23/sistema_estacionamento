from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey

class Parking(Base):
    __tablename__ = "parking"

    id = Column(Integer, primary_key=True, index=True)
    hora_entrada = Column(DateTime, nullable=False)
    hora_saida = Column(DateTime, nullable=True)
    cliente_id = Column(Integer, ForeignKey("clients.id"), nullable=False)

    pagamento = relationship("Payment", back_populates="estacionamento")
