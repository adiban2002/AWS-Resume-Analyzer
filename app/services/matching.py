from app.services.sagemaker_service import get_similarity_score
from app.services.scoring import calculate_score


def match_resume_with_jd(resume_text: str, jd_text: str):

    result = get_similarity_score(resume_text, jd_text)

    if "error" in result:
        return result

    similarity = result.get("similarity_score", 0)

    score_data = calculate_score(similarity)

    return {
        "similarity_score": similarity,
        **score_data
    }