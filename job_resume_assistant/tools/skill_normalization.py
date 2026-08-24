SKILL_ALIASES = {
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "gen ai": "generative ai",
    "genai": "generative ai",
    "postgres": "postgresql",
}


def normalize_skill(skill: str) -> str:
    normalized_skill = skill.strip().lower()

    return SKILL_ALIASES.get(
        normalized_skill,
        normalized_skill
    )