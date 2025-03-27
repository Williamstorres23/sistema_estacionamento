from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.auth_service import gerar_hash_senha, criar_token_acesso, autenticar_usuario
from app.models.user import User, UserRole
from app.schemas.user_schema import UserCreate, UserLogin


router = APIRouter()

@router.post("/register/")
def registrar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="E-mail já registrado")

    usuario = User(
        nome=user.nome,
        email=user.email,
        senha_hash=gerar_hash_senha(user.senha),
        role=user.role
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return {"message": "Usuário registrado com sucesso"}

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, user.email, user.senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token_acesso({"sub": usuario.email, "role": usuario.role})
    return {"access_token": token, "token_type": "bearer"}
