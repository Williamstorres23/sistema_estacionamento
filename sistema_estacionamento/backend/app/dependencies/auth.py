from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.user import User
from app.services.user_service import SECRET_KEY, ALGORITHM

# Configuração do esquema de autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/")

# Função para obter o usuário autenticado a partir do token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # Decodifica o token JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
        cargo = payload.get("cargo")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    
    # Busca o usuário no banco de dados
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    
    return {"user_id": user.id, "cargo": user.cargo}

# Função para verificar se o usuário é um administrador
def verificar_admin(user: dict = Depends(get_current_user)):
    if user["cargo"] != "Administrador":
        raise HTTPException(status_code=403, detail="Acesso negado. Apenas administradores podem acessar.")
    return user
