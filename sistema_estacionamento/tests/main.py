# Estrutura inicial do sistema de estacionamento com FastAPI

# Dockerfile para configurar o ambiente
# docker-compose.yml para gerenciar os containers
# Estrutura MVC com pastas organizadas
# Banco de dados PostgreSQL com tabelas estruturadas
# CRUDs completos e autenticação de usuários
# Rotas, serviços e repositórios organizados
# Configuração de logs e segurança
# Documentação e Pitch no Canva

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from app.routes import vehicle_routes, client_routes, parking_routes
from app.routes import notification_routes
from app.routes import payment_routes
from app.routes import report_routes
from app.routes import protected_routes
from app.routes import report_routes

app = FastAPI()

# Registro das rotas
app.include_router(vehicle_routes.router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(client_routes.router, prefix="/clients", tags=["Clients"])
app.include_router(parking_routes.router, prefix="/parking", tags=["Parking"])
app.include_router(notification_routes.router, prefix="/notifications", tags=["Notificações"])
app.include_router(payment_routes.router, prefix="/payments", tags=["Pagamentos"])
app.include_router(report_routes.router, prefix="/reports", tags=["Relatórios"])
app.include_router(protected_routes.router, prefix="/protected", tags=["Protected Routes"])
app.include_router(report_routes.router, prefix="/reports", tags=["Reports"])


@app.get("/")
def read_root():
    return {"message": "Sistema de estacionamento rodando"}