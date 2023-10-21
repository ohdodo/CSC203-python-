from dataclasses import dataclass
from prettytable import PrettyTable

@dataclass
class Job:
    job_id: int
    profit: int
    deadline: int

def input_jobs():
    try:
        n = int(input("Enter the number of jobs: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return []

    jobs = []
    for i in range(1, n + 1):
        try:
            profit = int(input(f"Enter the profit for job {i}: "))
            deadline = int(input(f"Enter the deadline for job {i}: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            return []
        jobs.append(Job(i, profit, deadline))
    
    table = PrettyTable()
    table.field_names = ["Job ID", "Profit", "Deadline"]
    for job in jobs:
        table.add_row([job.job_id, job.profit, job.deadline])
    
    print("Jobs Available:")
    print(table)

    return jobs

def sort_jobs(jobs):
    return sorted(jobs, key=lambda job: job.profit, reverse=True)

def schedule_jobs(jobs):
    n = len(jobs)
    slots = [False] * n
    schedule = []
    for i in range(n):
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                schedule.append((jobs[i], j))
                break
    return schedule

def print_schedule(schedule):
    table = PrettyTable(["Time Slot", "Job"])
    for job, time_slot in schedule:
        table.add_row([time_slot, job.job_id])
    print("Optimal Job Schedule:")
    print(table)


def main():
    print("\t\tJOB SEQUENCING PROGRAM\n\n")
    jobs = input_jobs()
    if not jobs:
        return  # Exit if there was an error in input
    sorted_jobs = sort_jobs(jobs)
    schedule = schedule_jobs(sorted_jobs)
    print_schedule(schedule)
    
    total_profit = sum(job[0].profit for job in schedule)
    print(f"Total profit of scheduled jobs: {total_profit}")

if __name__ == "__main__":
    main()
