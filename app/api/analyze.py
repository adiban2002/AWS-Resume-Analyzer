from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_utils import save_upload_file
from app.services.preprocessing import extract_text_from_pdf
from app.services.matching import match_resume_with_jd
from app.services.recommendations import generate_recommendations
from app.services.dynamodb_service import save_analysis

router = APIRouter()


@router.post("/analyze-match")
async def analyze_match(resume: UploadFile = File(...), jd: UploadFile = File(...)):

    if not resume.filename.endswith(".pdf") or not jd.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    resume_path = save_upload_file(resume)
    jd_path = save_upload_file(jd)

    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_pdf(jd_path)

    match_result = match_resume_with_jd(resume_text, jd_text)

    if "error" in match_result:
        raise HTTPException(status_code=500, detail=match_result)

    recommendations = []

    if match_result["assessment"] == "Low Match":
        recommendations = [
            "Your resume has low alignment with this job description.",
            "Consider tailoring your resume to better match the job requirements."
        ]
    elif match_result["assessment"] == "Moderate Match":
        recommendations = [
            "Your resume partially aligns with this job.",
            "Enhance relevant skills and experiences for stronger impact."
        ]
    else:
        recommendations = ["Great alignment with the job description!"]

    result = {
        "resume_filename": resume.filename,
        "jd_filename": jd.filename,
        "similarity_score": match_result["similarity_score"],
        "match_percentage": match_result["match_percentage"],
        "assessment": match_result["assessment"],
        "recommendations": recommendations
    }

    analysis_id = save_analysis(result)

    return {
        "analysis_id": analysis_id,
        **result
    }