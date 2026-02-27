from fastapi import APIRouter
from app.services.dynamodb_service import list_analyses, get_analysis

router = APIRouter()

@router.get("/history")
def history():
    return list_analyses()


@router.get("/history/{analysis_id}")
def fetch_analysis(analysis_id: str):
    return get_analysis(analysis_id)