from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.dependencies.auth import verificar_admin
from app.services.report_service import (
    total_veiculos_estacionados,
    faturamento_total,
    veiculos_por_periodo,
    faturamento_por_periodo
)
from app.database.connection import get_db

router = APIRouter()

@router.get("/veiculos-ativos/")
def get_veiculos_ativos(db: Session = Depends(get_db), admin: dict = Depends(verificar_admin)):
    total = total_veiculos_estacionados(db)
    return {"total_veiculos_estacionados": total}

@router.get("/faturamento-total/")
def get_faturamento_total(db: Session = Depends(get_db), admin: dict = Depends(verificar_admin)):
    pagamentos = faturamento_total(db)
    total = sum([p[0] for p in pagamentos])  # Somando os valores
    return {"faturamento_total": total}

@router.get("/veiculos-periodo/")
def get_veiculos_periodo(inicio: str, fim: str, db: Session = Depends(get_db), admin: dict = Depends(verificar_admin)):
    inicio_data = datetime.strptime(inicio, "%Y-%m-%d")
    fim_data = datetime.strptime(fim, "%Y-%m-%d")
    total = veiculos_por_periodo(db, inicio_data, fim_data)
    return {"veiculos_periodo": total}

@router.get("/faturamento-periodo/")
def get_faturamento_periodo(inicio: str, fim: str, db: Session = Depends(get_db), admin: dict = Depends(verificar_admin)):
    inicio_data = datetime.strptime(inicio, "%Y-%m-%d")
    fim_data = datetime.strptime(fim, "%Y-%m-%d")
    pagamentos = faturamento_por_periodo(db, inicio_data, fim_data)
    total = sum([p[0] for p in pagamentos])
    return {"faturamento_periodo": total}
