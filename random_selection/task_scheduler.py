"""
Task Scheduler


Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different
task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could
complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter
in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

"""
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hashmap to store frequencies of tasks
        tasks_list = Counter(tasks).values()
        # sort to find the task which occurs Maximum
        tasks_list = sorted(tasks_list, reverse=True)
        max_task = tasks_list[0]
        # find how many tasks are there which occur maximum number of times
        max_task_count = tasks_list.count(max_task)
        # apply formula that we derived after considering different cases
        interval = (max_task - 1) * (n + 1) + max_task_count

        return max(interval, len(tasks))
