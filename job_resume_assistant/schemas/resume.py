from pydantic import BaseModel, Field


class ResumeAnalysis(BaseModel):
    skills: list[str] | None = Field(
        default=None,
        description="Skills explicitly mentioned in the resume"
    )

    education: list[str] | None = Field(
        default=None,
        description="Education details explicitly mentioned in the resume"
    )

    experience: list[str] | None = Field(
        default=None,
        description="Work experience explicitly mentioned in the resume"
    )

    projects: list[str] | None = Field(
        default=None,
        description="Projects explicitly mentioned in the resume"
    )

    certifications: list[str] | None = Field(
        default=None,
        description="Certifications explicitly mentioned in the resume"
    )