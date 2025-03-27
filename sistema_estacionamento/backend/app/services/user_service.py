from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

# Configuração do Hash de Senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuração do JWT
SECRET_KEY = "chave_secreta_super_segura"
ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 60

def hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)

def criar_usuario(db: Session, user: UserCreate):
    senha_hash = hash_senha(user.senha)
    db_user = User(nome=user.nome, email=user.email, senha=senha_hash, cargo=user.cargo)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def autenticar_usuario(db: Session, email: str, senha: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verificar_senha(senha, user.senha):
        return None
    return user

def gerar_token_jwt(user_id: int, cargo: str):
    expiracao = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    payload = {"sub": str(user_id), "cargo": cargo, "exp": expiracao}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
