"""
n number of tasks -> t1, t2, tn
Each task has m subtasks -> t1 -> ts1, ts2 => status - in progress, success, failed
task_id -> Current status of task based on status of each subtask


"""
from typing import List



def get_subtask(subtask_id):
    pass


def task_status(subtasks: List[int]) -> str:
    wip_list, success_list = [], []

    for subtask_id in subtasks:
        if current_time > threshold_time:
            subtask = get_subtask(subtask_id)
        else:
            subtask.task = subtask_id[status]

        if subtask.status == "failed":
            return "Failed"
        elif subtask.status == "In progress":
            return "In progress"
    return "Success"

"""
supervisor -> 1
parallel => determine 

t[] = [chunk for x from list of tasks]

for each_chunk in chunks:
    process_id[] = task_status_process(each_chunk)


subtask_id => threshold_time => status
1 => 123 => In progress
subtask


How to determine the threshold e.g. 200ms
How to handle the first load?

Precomupation based on the need => Is it regular load? Is it some festival load?
Can we de


How long a certain status is valid => 200ms

[subtask_id => subtask_status] # O(1)

final_status => Flag => 

"""