from sqlalchemy.orm import Session
from app.models.models import Veiculo
from app.schemas.schemas import VeiculoSchema

# Criar um novo veículo
def criar_veiculo(db: Session, veiculo: VeiculoSchema):
    novo_veiculo = Veiculo(
        placa=veiculo.placa,
        modelo=veiculo.modelo,
        cor=veiculo.cor,
        proprietario_id=veiculo.proprietario_id
    )
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    return novo_veiculo

# Obter todos os veículos
def listar_veiculos(db: Session):
    return db.query(Veiculo).all()

# Obter um veículo por ID
def obter_veiculo_por_id(db: Session, veiculo_id: int):
    return db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()

# Atualizar um veículo
def atualizar_veiculo(db: Session, veiculo_id: int, veiculo: VeiculoSchema):
    db_veiculo = obter_veiculo_por_id(db, veiculo_id)
    if db_veiculo:
        db_veiculo.placa = veiculo.placa
        db_veiculo.modelo = veiculo.modelo
        db_veiculo.cor = veiculo.cor
        db_veiculo.proprietario_id = veiculo.proprietario_id
        db.commit()
        db.refresh(db_veiculo)
    return db_veiculo

# Deletar um veículo
def deletar_veiculo(db: Session, veiculo_id: int):
    db_veiculo = obter_veiculo_por_id(db, veiculo_id)
    if db_veiculo:
        db.delete(db_veiculo)
        db.commit()
    return db_veiculo
