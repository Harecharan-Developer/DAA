from job_sequencing import Job, job_sequencing_branch_bound



def test_job_sequencing_branch_bound():
    # Test case 1: Jobs with different deadlines and profits
    jobs1 = [Job('J1', 2, 60), Job('J2', 1, 100), Job('J3', 3, 20), Job('J4', 2, 40)]
    sequence1, profit1 = job_sequencing_branch_bound(jobs1)
    assert sequence1 == ['J2', 'J1', 'J4']
    assert profit1 == 200

    # Test case 2: Jobs with same deadlines but different profits
    jobs2 = [Job('J1', 2, 60), Job('J2', 2, 100), Job('J3', 2, 20), Job('J4', 2, 40)]
    sequence2, profit2 = job_sequencing_branch_bound(jobs2)
    assert sequence2 == ['J2', 'J1']
    assert profit2 == 160

    # Test case 3: Jobs with same profits but different deadlines
    jobs3 = [Job('J1', 2, 60), Job('J2', 1, 60), Job('J3', 3, 60), Job('J4', 2, 60)]
    sequence3, profit3 = job_sequencing_branch_bound(jobs3)
    assert sequence3 == ['J1', 'J4', 'J3']
    assert profit3 == 180

    # Test case 4: Empty job list
    jobs4 = []
    sequence4, profit4 = job_sequencing_branch_bound(jobs4)
    assert sequence4 == []
    assert profit4 == 0

    print("All test cases passed!")

test_job_sequencing_branch_bound()


def test_job_sequencing_branch_bound():
    # Test case 1: Jobs with different deadlines and profits
    jobs1 = [Job('J1', 2, 60), Job('J2', 1, 100), Job('J3', 3, 20), Job('J4', 2, 40)]
    sequence1, profit1 = job_sequencing_branch_bound(jobs1)
    assert sequence1 == ['J2', 'J1', 'J4']
    assert profit1 == 200

    # Test case 2: Jobs with same deadlines but different profits
    jobs2 = [Job('J1', 2, 60), Job('J2', 2, 100), Job('J3', 2, 20), Job('J4', 2, 40)]
    sequence2, profit2 = job_sequencing_branch_bound(jobs2)
    assert sequence2 == ['J2', 'J1']
    assert profit2 == 160

    # Test case 3: Jobs with same profits but different deadlines
    jobs3 = [Job('J1', 2, 60), Job('J2', 1, 60), Job('J3', 3, 60), Job('J4', 2, 60)]
    sequence3, profit3 = job_sequencing_branch_bound(jobs3)
    assert sequence3 == ['J1', 'J4', 'J3']
    assert profit3 == 180

    # Test case 4: Empty job list
    jobs4 = []
    sequence4, profit4 = job_sequencing_branch_bound(jobs4)
    assert sequence4 == []
    assert profit4 == 0

    print("All test cases passed!")

test_job_sequencing_branch_bound()