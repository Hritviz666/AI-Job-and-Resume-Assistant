from chains.job_chain import job_chain


job_description = input(
    "Paste the job description:\n"
)


response = job_chain.invoke({
    "job_description": job_description
})


print("\n--- JOB ANALYSIS ---")

print("\nJob Title:")
print(response.job_title)

print("\nRequired Skills:")
print(response.required_skills)

print("\nPreferred Skills:")
print(response.preferred_skills)

print("\nResponsibilities:")
print(response.responsibilities)

print("\nExperience:")
print(response.experience_level)

print("\nEducation:")
print(response.education)