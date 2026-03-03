def calculate_score(similarity_score: float):
    """
    Takes similarity score (0 to 1) from SageMaker
    and converts it to percentage + assessment.
    """

    percentage = similarity_score * 100

    if percentage >= 80:
        level = "Strong Match"
    elif percentage >= 50:
        level = "Moderate Match"
    else:
        level = "Low Match"

    return {
        "match_percentage": round(percentage, 2),
        "assessment": level
    }