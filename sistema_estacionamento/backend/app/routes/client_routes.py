from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repositories.client_repository import (
    criar_cliente, listar_clientes, obter_cliente_por_id, atualizar_cliente, deletar_cliente
)
from app.schemas.schemas import ClienteSchema
from database.connection import get_db

router = APIRouter()

# Criar um novo cliente
@router.post("/", response_model=ClienteSchema)
def criar(cliente: ClienteSchema, db: Session = Depends(get_db)):
    return criar_cliente(db, cliente)

# Listar todos os clientes
@router.get("/", response_model=list[ClienteSchema])
def listar(db: Session = Depends(get_db)):
    return listar_clientes(db)

# Obter um cliente por ID
@router.get("/{cliente_id}", response_model=ClienteSchema)
def obter(cliente_id: int, db: Session = Depends(get_db)):
    cliente = obter_cliente_por_id(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

# Atualizar um cliente
@router.put("/{cliente_id}", response_model=ClienteSchema)
def atualizar(cliente_id: int, cliente: ClienteSchema, db: Session = Depends(get_db)):
    return atualizar_cliente(db, cliente_id, cliente)

# Deletar um cliente
@router.delete("/{cliente_id}")
def deletar(cliente_id: int, db: Session = Depends(get_db)):
    cliente = deletar_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"message": "Cliente deletado com sucesso"}
