def match_skills(resume_skills: list, jd_skills: list):
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    matched = resume_set.intersection(jd_set)
    missing = jd_set.difference(resume_set)

    return {
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing)),
        "total_required": len(jd_set),
        "matched_count": len(matched)
    }