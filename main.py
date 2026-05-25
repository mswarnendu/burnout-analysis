import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mental_health_burnout_tech_2026.csv")

job_list = df["job_role"]
score_list = df["burnout_score"]

total_list = list(zip(job_list, score_list))

job_count = {}
organized = {}

for job, score in total_list:
    if job not in organized.keys() and score >= 5:
        organized[job] = 1
    elif score >= 5:
        organized[job] += 1

    if job not in job_count.keys():
        job_count[job] = 1
    else:
        job_count[job] += 1

all_possible_jobs = []
rates_list = []

for job in job_count.keys():
    print(
        f"Rate of a burnout score over 5 among {job}: {(organized[job]/job_count[job] * 100):.2f}%")
    all_possible_jobs.append(job.split(" ")[0][0:3])
    rates_list.append((organized[job]/job_count[job]) * 100)

unified_list = list(zip(all_possible_jobs, rates_list))

max_rate = 0
max_tuple = ()

for job, rate in unified_list:
    if rate > max_rate:
        max_rate = rate
        max_tuple = (job, rate)

print()
print(
    f"The job with the highest burnout rate is {max_tuple[0]}, with a rate of a burnout score over 5 of {max_tuple[1]:.2f}%")

plt.bar(all_possible_jobs, rates_list)
plt.title("Burnout Rates per Job in Tech")
plt.xlabel("Job")
plt.ylabel("Burnout Rate (in %)")
plt.legend()
plt.grid(True)
plt.show()
