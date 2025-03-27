from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from sqlalchemy.orm import Session
from app.models.user import User, UserRole
from app.database.connection import get_db

# Configuração da criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def gerar_hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)

def criar_token_acesso(dados: dict):
    dados_expiracao = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados_expiracao.update({"exp": expiracao})
    return jwt.encode(dados_expiracao, SECRET_KEY, algorithm=ALGORITHM)

def autenticar_usuario(db: Session, email: str, senha: str):
    usuario = db.query(User).filter(User.email == email).first()
    if usuario and verificar_senha(senha, usuario.senha_hash):
        return usuario
    return None
