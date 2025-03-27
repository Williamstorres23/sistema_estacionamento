from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Esquema para Cliente
class ClienteSchema(BaseModel):
    nome: str
    contato: str
    historico: Optional[str] = None

# Esquema para Veículo
class VeiculoSchema(BaseModel):
    placa: str
    modelo: str
    cor: str
    proprietario_id: int

# Esquema para Estacionamento
class EstacionamentoSchema(BaseModel):
    veiculo_id: int
    entrada: Optional[datetime] = None
    saida: Optional[datetime] = None
    valor_pago: Optional[float] = None
