from fastapi import APIRouter, BackgroundTasks
from app.services.notification_service import enviar_notificacao

router = APIRouter()

@router.post("/notificar-tempo-excedido/")
async def notificar_tempo_excedido(background_tasks: BackgroundTasks, email: str, placa: str, tempo: int):
    mensagem = f"O veículo de placa {placa} ultrapassou o tempo de {tempo} minutos."
    background_tasks.add_task(enviar_notificacao, email, "Alerta de Tempo Excedido", mensagem)
    return {"status": "Notificação enviada"}
