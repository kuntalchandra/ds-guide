"""
Meeting Rooms I

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine
if a person could attend all meetings.
For example,
Given [[0, 30],[5, 10],[15, 20]],
return false


Approach:
Sort by start time. Walk through pairs of consecutive meetings.
If the previous meeting's end time overlaps with the next start,
you can't attend all — return False immediately.

intervals.sort(key=lambda interval: interval[0])
for idx in range(1, len(intervals)):
    next_start, next_end = intervals[idx]
    if prev_end > next_start:   # overlap = conflict
        return False
    prev_end = next_end
return True

Time: O(n log n) — sort dominates
Space: O(1) — sort in-place, scan with two variables

Triggers:
- can one person attend all meetings
- overlap detection after sorting
- baseline before Meeting Rooms II

Variants / Watch-outs:
- Optimisation angle: the naive O(n²) approach checks every pair — sort first, then
  one linear pass is all you need
- Boundary condition: end == next_start is NOT a conflict (half-open intervals [s, e))



Time complexity: O(nLogn)
Space complexity: O(n)
"""
from typing import List
from unittest import TestCase


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda n: n[0])
        start, end = intervals[0]
        for idx in range(1, len(intervals)):
            next_start, next_end = intervals[idx]
            if end > next_start:
                return False
            start, end = next_start, next_end
        return True


class TestMeetingRoom(TestCase):
    def setUp(self) -> None:
        self.meetings_1 = [[0, 30], [5, 10], [15, 20]]
        self.meetings_2 = [[7, 10], [2, 4]]
        self.meetings_3 = [[13, 15], [1, 13]]

    def test_meeting_rooms(self) -> None:
        obj = Solution()
        self.assertFalse(obj.canAttendMeetings(self.meetings_1))
        self.assertTrue(obj.canAttendMeetings(self.meetings_2))
        self.assertTrue(obj.canAttendMeetings(self.meetings_3))
