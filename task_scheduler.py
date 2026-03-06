"""
Problem:
Given a list of tasks (each a letter A-Z) and a cooldown n, find the minimum
intervals (CPU slots) needed to finish all tasks. Same task must be at least
n intervals apart. CPU can be idle.

Example:
tasks = ["A","A","A","B","B","B"], n = 2
Output: 8  (A→B→idle→A→B→idle→A→B)

tasks = ["A","A","A","B","B","B"], n = 0
Output: 6

Approach:
The most frequent task determines the structure. If max_freq tasks appear f times,
they create (f - 1) "chunks" of size (n + 1), plus a final partial chunk.
Formula: max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq_tasks)

from collections import Counter
count = Counter(tasks)
max_freq = max(count.values())
count_of_max = sum(1 for freq in count.values() if freq == max_freq)

slots = (max_freq - 1) * (n + 1) + count_of_max
return max(len(tasks), slots)

Time: O(n) to count + O(1) formula
Space: O(1) — at most 26 task types

Triggers:
- cooldown between same task type
- CPU scheduling / job scheduling with constraints
- "minimum time to complete all tasks"

Variants / Watch-outs:
- Optimisation angle: heap-based simulation is O(n log 26) = O(n) and more intuitive but
  the formula is O(n) with much less code — know both
- The formula handles the case where tasks fill all slots with no idle needed:
  max() picks len(tasks) when idle slots would be negative
- Reorganise String (LC 767): same idea — can you arrange so no two same chars are adjacent?
  Answer: possible iff max_freq <= (len(s) + 1) // 2
"""