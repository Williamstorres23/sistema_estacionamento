import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from app.config import EMAIL_USER, EMAIL_PASSWORD, TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE

# Função para enviar e-mail
def enviar_email(destinatario, assunto, mensagem):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(mensagem, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, destinatario, msg.as_string())
        server.quit()
        return {"message": "E-mail enviado com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

# Função para enviar SMS usando Twilio
def enviar_sms(numero_destino, mensagem):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"
    data = {
        "From": TWILIO_PHONE,
        "To": numero_destino,
        "Body": mensagem,
    }

    try:
        response = requests.post(url, data=data, auth=(TWILIO_SID, TWILIO_AUTH_TOKEN))
        return response.json()
    except Exception as e:
        return {"error": str(e)}
