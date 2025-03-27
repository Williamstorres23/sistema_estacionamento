from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.services.report_service import ReportService
from database.connection import get_db

router = APIRouter()

@router.get("/relatorio-pdf/", response_class=StreamingResponse)
def download_pdf(db: Session = Depends(get_db)):
    pdf_buffer = ReportService.generate_pdf_report(db)
    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=relatorio.pdf"})
