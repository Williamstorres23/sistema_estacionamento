from sqlalchemy import Column, Integer, String
from app.database.connection import Base
from app.database.connection import Base, engine, get_db



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)  # Será armazenada de forma segura (hash)
    cargo = Column(String, nullable=False)  # "Funcionario" ou "Administrador"
