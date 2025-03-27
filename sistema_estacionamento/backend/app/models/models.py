from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from database.connection import Base
import datetime

# Modelo de Cliente
class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    contato = Column(String, nullable=False)
    historico = Column(String, nullable=True)

# Modelo de Veículo
class Veiculo(Base):
    __tablename__ = "veiculos"
    
    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True, nullable=False)
    modelo = Column(String, nullable=False)
    cor = Column(String, nullable=False)
    proprietario_id = Column(Integer, ForeignKey("clientes.id"))

    proprietario = relationship("Cliente")

# Modelo de Controle de Estacionamento
class Estacionamento(Base):
    __tablename__ = "estacionamento"
    
    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"))
    entrada = Column(DateTime, default=datetime.datetime.utcnow)
    saida = Column(DateTime, nullable=True)
    valor_pago = Column(Float, nullable=True)

    veiculo = relationship("Veiculo")
