from app.services.nlp_engine import extract_skills

def parse_job_description(text: str):
    skills = extract_skills(text)

    return {
        "required_skills": skills
    }