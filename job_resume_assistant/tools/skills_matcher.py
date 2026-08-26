from schemas.job import SkillMatch
from tools.skill_normalization import normalize_skill


def compare_skills(
    target_skills: list[str] | None,
    candidate_skills: list[str] | None
) -> SkillMatch:

    target_skills = target_skills or []
    candidate_skills = candidate_skills or []

    candidate_set = {
        normalize_skill(skill)
        for skill in candidate_skills
    }

    seen_target_skills = set()

    matching_skills = []
    missing_skills = []

    for skill in target_skills:
        normalized_skill = normalize_skill(skill)

        if normalized_skill in seen_target_skills:
            continue

        seen_target_skills.add(normalized_skill)

        if normalized_skill in candidate_set:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    return SkillMatch(
        matching_skills=matching_skills,
        missing_skills=missing_skills
    )