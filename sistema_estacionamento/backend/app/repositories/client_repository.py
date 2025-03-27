from sqlalchemy.orm import Session
from app.models.models import Cliente
from app.schemas.schemas import ClienteSchema

# Criar um novo cliente
def criar_cliente(db: Session, cliente: ClienteSchema):
    novo_cliente = Cliente(nome=cliente.nome, contato=cliente.contato, historico=cliente.historico)
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

# Obter todos os clientes
def listar_clientes(db: Session):
    return db.query(Cliente).all()

# Obter um cliente por ID
def obter_cliente_por_id(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

# Atualizar um cliente
def atualizar_cliente(db: Session, cliente_id: int, cliente: ClienteSchema):
    db_cliente = obter_cliente_por_id(db, cliente_id)
    if db_cliente:
        db_cliente.nome = cliente.nome
        db_cliente.contato = cliente.contato
        db_cliente.historico = cliente.historico
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

# Deletar um cliente
def deletar_cliente(db: Session, cliente_id: int):
    db_cliente = obter_cliente_por_id(db, cliente_id)
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente
