from tools.skills_matcher import compare_skills
from chains.analysis_chain import analysis_chain
from tools.skill_normalization import normalize_skill

print(normalize_skill("ML"))
print(normalize_skill("  GenAI  "))
print(normalize_skill("Postgres"))
print(normalize_skill("PyTorch"))

job_description = input(
    "Paste the job description:\n"
)


resume_text = """
Name: Alex

Skills:
Python, ML, Postgres

Education:
B.Tech in Computer Science

"""

result = analysis_chain.invoke({
    "job_description": job_description,
    "resume": resume_text
})

match_result = compare_skills(
    required_skills=result["job"].required_skills,
    candidate_skills=result["resume"].skills
)

print(match_result.matching_skills)
print(match_result.missing_skills)

