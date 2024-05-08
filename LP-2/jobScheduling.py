class Job():
    def __init__(self,id,deadline,duration):

        self.id, self.deadline, self.duration = id, deadline, duration

jobs = [Job("Job1", 5, 2), Job("Job2", 3, 1), Job("Job3", 8, 2), Job("Job4", 6, 3),Job("Job5", 7, 1)]


def greedy(jobs):
    current = 0
    schedule = []

    jobs = sorted(jobs, key= lambda j: j.deadline)

    for job in jobs:
        if job.duration + current<=job.deadline:
            schedule.append((job.id, current, job.duration+ current))
            current += job.duration

    return schedule

schedule = greedy(jobs)

for job in schedule:
        print("Job:", job[0], "| Start Time:", job[1], "| End Time:", job[2])