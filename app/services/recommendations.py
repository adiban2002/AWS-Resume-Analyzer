def generate_recommendations(missing_skills: list):
    if not missing_skills:
        return ["Your profile aligns well with this job."]

    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Consider learning or highlighting {skill}")

    return suggestions