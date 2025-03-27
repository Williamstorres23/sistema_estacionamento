from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repositories.vehicle_repository import (
    criar_veiculo, listar_veiculos, obter_veiculo_por_id, atualizar_veiculo, deletar_veiculo
)
from app.schemas.schemas import VeiculoSchema
from database.connection import get_db

router = APIRouter()

# Criar um novo veículo
@router.post("/", response_model=VeiculoSchema)
def criar(veiculo: VeiculoSchema, db: Session = Depends(get_db)):
    return criar_veiculo(db, veiculo)

# Listar todos os veículos
@router.get("/", response_model=list[VeiculoSchema])
def listar(db: Session = Depends(get_db)):
    return listar_veiculos(db)

# Obter um veículo por ID
@router.get("/{veiculo_id}", response_model=VeiculoSchema)
def obter(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = obter_veiculo_por_id(db, veiculo_id)
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo

# Atualizar um veículo
@router.put("/{veiculo_id}", response_model=VeiculoSchema)
def atualizar(veiculo_id: int, veiculo: VeiculoSchema, db: Session = Depends(get_db)):
    return atualizar_veiculo(db, veiculo_id, veiculo)

# Deletar um veículo
@router.delete("/{veiculo_id}")
def deletar(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = deletar_veiculo(db, veiculo_id)
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return {"message": "Veículo deletado com sucesso"}
