from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str
    cargo: str  # "Funcionario" ou "Administrador"

class UserLogin(BaseModel):
    email: str
    senha: str
