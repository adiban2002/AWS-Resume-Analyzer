def match_skills(resume_skills: list, jd_skills: list):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = resume_set.intersection(jd_set)
    missing = jd_set.difference(resume_set)

    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "total_required": len(jd_set),
        "matched_count": len(matched)
    }