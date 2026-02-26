from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_utils import save_upload_file
from app.services.preprocessing import extract_text_from_pdf

router = APIRouter()

@router.post("/upload-jd")
async def upload_job_description(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    file_path = save_upload_file(file)

    extracted_text = extract_text_from_pdf(file_path)

    return {
        "jd_filename": file.filename,
        "characters_extracted": len(extracted_text),
        "preview": extracted_text[:500]
    }