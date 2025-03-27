from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime
from app.repositories.report_repository import ReportRepository

class ReportService:
    @staticmethod
    def generate_pdf_report(db):
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        pdf.setTitle("Relatório de Estacionamento")

        # Cabeçalho
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(200, 750, "Relatório de Estacionamento")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(200, 730, f"Data de emissão: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

        # Puxar dados do banco
        total_veiculos = ReportRepository.get_total_vehicles(db)
        faturamento_total = ReportRepository.get_total_revenue(db)

        # Conteúdo do Relatório
        pdf.drawString(100, 680, f"Total de Veículos Estacionados: {total_veiculos}")
        pdf.drawString(100, 660, f"Faturamento Total: R$ {faturamento_total:.2f}")

        # Finalizar PDF
        pdf.showPage()
        pdf.save()
        buffer.seek(0)

        return buffer
