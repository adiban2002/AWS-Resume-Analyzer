from app.utils.text_utils import clean_text
from app.config import SKILL_KEYWORDS


def extract_skills_from_text(text: str):

    cleaned_text = clean_text(text)

    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill.lower() in cleaned_text:
            found_skills.append(skill.lower())

    return list(set(found_skills))


def parse_resume(text: str):
    skills = extract_skills_from_text(text)

    return {
        "skills": skills,
        "text_length": len(text)
    }