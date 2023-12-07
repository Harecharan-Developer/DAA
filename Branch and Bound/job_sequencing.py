class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_branch_bound(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    n = len(jobs)
    result = [-1] * n  # To store the final sequence
    slot = [False] * n  # To track the availability of time slots
    total_profit = 0  # To store the maximum total profit

    def is_valid(slot_index, curr_job):
        # Check if the current job can be assigned to the given time slot
        return slot[slot_index] is False and jobs[curr_job].deadline >= slot_index + 1

    def branch_and_bound_util(curr_job, profit_so_far):
        nonlocal total_profit

        if curr_job == n:
            return

        # Try assigning the current job to different time slots
        for i in range(min(n, jobs[curr_job].deadline) - 1, -1, -1):
            if is_valid(i, curr_job):
                result[i] = jobs[curr_job].id
                slot[i] = True
                profit_so_far += jobs[curr_job].profit

                # Update the total profit if the current assignment is more profitable
                if profit_so_far > total_profit:
                    total_profit = profit_so_far

                # Recur for the next job
                branch_and_bound_util(curr_job + 1, profit_so_far)

                # Backtrack: undo the current assignment
                result[i] = -1
                slot[i] = False
                profit_so_far -= jobs[curr_job].profit

    branch_and_bound_util(0, 0)

    final_result = [job.id for job_id in result if job_id != -1]
    return final_result, total_profit

# Example usage:
jobs = [Job('J1', 2, 60), Job('J2', 1, 100), Job('J3', 3, 20), Job('J4', 2, 40)]
sequence, profit = job_sequencing_branch_bound(jobs)
print("Job Sequence:", sequence)
print("Total Profit:", profit)
