from sqlalchemy.orm import Session
from app.models.models import Estacionamento
from app.schemas.schemas import EstacionamentoSchema
from datetime import datetime

# Registrar entrada no estacionamento
def registrar_entrada(db: Session, estacionamento: EstacionamentoSchema):
    novo_registro = Estacionamento(
        veiculo_id=estacionamento.veiculo_id,
        entrada=datetime.utcnow()
    )
    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)
    return novo_registro

# Registrar saída e calcular pagamento
def registrar_saida(db: Session, estacionamento_id: int, valor_pago: float):
    registro = db.query(Estacionamento).filter(Estacionamento.id == estacionamento_id).first()
    if registro and registro.saida is None:
        registro.saida = datetime.utcnow()
        registro.valor_pago = valor_pago
        db.commit()
        db.refresh(registro)
    return registro

# Listar todas as entradas e saídas
def listar_registros(db: Session):
    return db.query(Estacionamento).all()

# Obter registro por ID
def obter_registro_por_id(db: Session, estacionamento_id: int):
    return db.query(Estacionamento).filter(Estacionamento.id == estacionamento_id).first()
