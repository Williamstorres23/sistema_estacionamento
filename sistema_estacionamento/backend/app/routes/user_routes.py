from app.models.user import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.user_service import criar_usuario, autenticar_usuario, gerar_token_jwt
from app.schemas.user_schema import UserCreate, UserLogin


router = APIRouter()

@router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(User).filter(User.email == user.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    novo_usuario = criar_usuario(db, user)
    return {"message": "Usuário criado com sucesso!", "user_id": novo_usuario.id}

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, user.email, user.senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    token = gerar_token_jwt(usuario.id, usuario.cargo)
    return {"access_token": token, "token_type": "bearer"}
