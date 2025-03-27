from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados (ajuste conforme necessário)
DATABASE_URL = "postgresql://admin:senha123@localhost:5432/estacionamento"

# Criando o motor do banco de dados
engine = create_engine(DATABASE_URL)

# Criando a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando a classe base para os modelos do SQLAlchemy
Base = declarative_base()

# Dependência para obter sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
