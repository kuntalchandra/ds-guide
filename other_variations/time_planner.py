"""
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting
duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no
common time slot that satisfies the duration requirement, return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have
elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first
epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input
variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair
represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a
person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12

"""


def meeting_planner(slotsA, slotsB, dur):
    i, j = 0, 0
    len_a, len_b = len(slotsA), len(slotsB)
    while i < len_a and j < len_b:
        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])

        if (start + dur) <= end:
            return [start, start + dur]
        if slotsA[i][1] < slotsB[j][1]:  # either or
            i += 1
        else:
            j += 1

    return []
