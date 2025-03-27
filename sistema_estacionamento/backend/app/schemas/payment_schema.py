from pydantic import BaseModel
from typing import Literal

class PaymentCreate(BaseModel):
    client_id: int
    vehicle_id: int
    amount: float
    payment_method: Literal["dinheiro", "cartão", "PIX"]
