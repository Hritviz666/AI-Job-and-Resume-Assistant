from tools.skills_matcher import compare_skills
from chains.analysis_chain import analysis_chain


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

required_match = compare_skills(
    target_skills=result["job"].required_skills,
    candidate_skills=result["resume"].skills
)

preferred_match = compare_skills(
    target_skills=result["job"].preferred_skills,
    candidate_skills=result["resume"].skills
)

print("Required Skills:")
print(required_match)

print("\nPreferred Skills:")
print(preferred_match)

