import re

SKILLS_DB = [
    "aws", "docker", "kubernetes", "python", "terraform",
    "ci/cd", "linux", "fastapi", "devops", "cloud",
    "s3", "ec2", "git", "jenkins"
]

def extract_skills(text: str):
    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return list(set(found_skills))