def compare_skills(
    required_skills: list[str] | None,
    candidate_skills: list[str] | None
):
    required_skills = required_skills or []
    candidate_skills = candidate_skills or []

    required_set = {skill.lower() for skill in required_skills}
    candidate_set = {skill.lower() for skill in candidate_skills}

    matching_skills = required_set & candidate_set
    missing_skills = required_set - candidate_set

    return {
        "matching_skills": list(matching_skills),
        "missing_skills": list(missing_skills)
    }