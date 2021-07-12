"""
University career fair
https://leetcode.com/discuss/interview-question/374846/Twitter-or-OA-2019-or-University-Career-Fair

Given a list of arrival time and a list of duration, find out maximum number of events that can be scheduled.

For example, n = 5 companies that will arrive at arrival = [1, 3, 3, 5, 7] and will stay for duration = [2, 2, 1, 2, 1].
The first company arrives at time 1 and stays for 2 hours. At time 3, two companies arrive, but only can stay for
either 1 hour or 2 hours as the stage will be occupied. The next companies arrive at times 5 and 7 and don't conflict
with each other. In total, there can be a maximum of 4 events scheduled.

Approach:
Interval scheduling algo- sort then greedy pick up
"""
from typing import List
from unittest import TestCase


def schedule_events(arrival: List[int], duration: List[int]) -> int:
    # Get the list of start and end time, sorted by start time, end time => [[1, 3], [3, 4], [3, 5], [5, 7], [7, 8]]
    interval = [[arrival[i], arrival[i] + duration[i]] for i in range(len(arrival))]
    interval.sort(key=lambda x: (x[0], x[1]))
    end_time = interval[0][1]
    conflicts = []
    for i in range(1, len(interval)):
        current_start, current_end = interval[i]
        if current_start < end_time:
            conflicts.append(1)
        else:
            end_time = current_end
    return len(arrival) - len(conflicts)


class TestScheduleEvents(TestCase):
    def setUp(self) -> None:
        self.arrival_1 = [1, 3, 3, 5, 7]
        self.duration_1 = [2, 2, 1, 2, 1]
        self.arrival_2 = [1, 2]
        self.duration_2 = [7, 3]
        self.arrival_3 = [1, 3, 4, 6]
        self.duration_3 = [4, 3, 3, 2]

    def test_schedule_events(self):
        self.assertEqual(4, schedule_events(self.arrival_1, self.duration_1))
        self.assertEqual(1, schedule_events(self.arrival_2, self.duration_2))
        self.assertEqual(2, schedule_events(self.arrival_3, self.duration_3))
