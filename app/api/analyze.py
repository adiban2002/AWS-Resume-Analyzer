from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_utils import save_upload_file
from app.services.preprocessing import extract_text_from_pdf
from app.services.nlp_engine import extract_skills
from app.services.matching import match_skills
from app.services.scoring import calculate_score
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

    
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    
    match_result = match_skills(resume_skills, jd_skills)

    
    score_result = calculate_score(
        match_result["matched_count"],
        match_result["total_required"]
    )

    
    recommendations = generate_recommendations(match_result["missing_skills"])

    
    result = {
        "resume_filename": resume.filename,
        "jd_filename": jd.filename,
        "resume_skills": resume_skills,
        "jd_required_skills": jd_skills,
        "match": match_result,
        "score": score_result,
        "recommendations": recommendations
    }

    
    analysis_id = save_analysis(result)

    
    return {
        "analysis_id": analysis_id,
        **result
    }