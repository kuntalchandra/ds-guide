"""
Meeting Rooms I

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine
if a person could attend all meetings.
For example,
Given [[0, 30],[5, 10],[15, 20]],
return false
Time complexity: O(nLogn)
Sace complexity: O(n)
"""
from typing import List
from unittest import TestCase


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda n: n[0])
        start, end = intervals[0][0], intervals[0][1]
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
