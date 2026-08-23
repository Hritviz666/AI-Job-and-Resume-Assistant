from chains.job_chain import job_chain
from chains.resume_chain import resume_chain
from tools.skills_matcher import compare_skills

# job_description = input(
#     "Paste the job description:\n"
# )


# response = job_chain.invoke({
#     "job_description": job_description
# })

result = compare_skills(
    required_skills=[
        "Python",
        "LangChain",
        "Docker"
    ],
    candidate_skills=[
        "python",
        "PyTorch"
    ]
)

print(result)

# resume_text = """

# Name: Alex

# Education:
# B.Tech in Computer Science

# Projects:
# Built a RAG chatbot

# Certifications:
# AWS Certified Cloud Practitioner
# """

# response = resume_chain.invoke({
#     "resume": resume_text
# })

# print(response)


# print("\n--- JOB ANALYSIS ---")

# print("\nJob Title:")
# print(response.job_title)

# print("\nRequired Skills:")
# print(response.required_skills)

# print("\nPreferred Skills:")
# print(response.preferred_skills)

# print("\nResponsibilities:")
# print(response.responsibilities)

# print("\nExperience:")
# print(response.experience_level)

# print("\nEducation:")
# print(response.education)