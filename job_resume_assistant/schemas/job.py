from pydantic import BaseModel, Field


class JobAnalysis(BaseModel):
    job_title: str | None = Field(
        default=None,
        description="Job title or role being offered"
    )

    required_skills: list[str] | None = Field(
        default=None,
        description="Technical and professional skills explicitly required"
    )

    preferred_skills: list[str] | None = Field(
        default=None,
        description="Skills that are preferred but not mandatory"
    )

    responsibilities: list[str] | None = Field(
        default=None,
        description="Main responsibilities of the role"
    )

    experience_level: str | None = Field(
        default=None,
        description="Required years or level of experience"
    )

    education: str | None = Field(
        default=None,
        description="Required or preferred educational qualification"
    )

class SkillMatch(BaseModel):
    matching_skills: list[str] = Field(
        default_factory=list,
        description="Skills found in both the job requirements and candidate skills."
    )

    missing_skills: list[str] = Field(
        default_factory=list,
        description="Required job skills not found in the candidate skills."
    )