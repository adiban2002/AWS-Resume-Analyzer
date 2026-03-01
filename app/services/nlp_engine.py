from app.models.resume_parser import parse_resume


def extract_skills(text: str):
    parsed_data = parse_resume(text)

    return parsed_data["skills"]