from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user, verificar_admin

router = APIRouter()

# Rota protegida que qualquer usuário autenticado pode acessar
@router.get("/user-info/")
def user_info(user: dict = Depends(get_current_user)):
    return {"message": "Bem-vindo!", "user_id": user["user_id"], "cargo": user["cargo"]}

# Rota exclusiva para administradores
@router.get("/admin-dashboard/")
def admin_dashboard(user: dict = Depends(verificar_admin)):
    return {"message": "Bem-vindo ao painel administrativo!", "admin_id": user["user_id"]}
