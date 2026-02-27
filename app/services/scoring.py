def calculate_score(matched_count: int, total_required: int):
    if total_required == 0:
        return 0

    score = (matched_count / total_required) * 100

    if score >= 80:
        level = "Strong Match"
    elif score >= 50:
        level = "Moderate Match"
    else:
        level = "Low Match"

    return {
        "match_percentage": round(score, 2),
        "assessment": level
    }