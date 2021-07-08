"""
Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the
minimum number of conference rooms required
For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2
Approach: : Sort the meetings based on start at first. If one meeting finishes and another meeting has no conflict with
finished one, then the corresponding room can be used by the following meeting. Let’s use a min heap to store the end
of finished meeting. After this process, the number of elements in min heap is the result
Time complexity: O(nLogn)
Space complexity: O(n)
"""
from heapq import heappop, heappush
from typing import List
from unittest import TestCase


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda n: n[0])  # By start time
        rooms = [intervals[0][1]]   # Default need
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= rooms[0]:  # 1 room got free, reuse
                heappop(rooms)
            heappush(rooms, end)
        return len(rooms)


class TestMeetingRoom(TestCase):
    def setUp(self) -> None:
        self.meetings_1 = [[0, 30], [5, 10], [15, 20]]
        self.meetings_2 = [[1, 5], [10, 11], [2, 3], [1, 2], [1, 3], [1, 2], [6, 8]]

    def test_meeting_rooms(self) -> None:
        obj = Solution()
        self.assertEqual(2, obj.minMeetingRooms(self.meetings_1))
        self.assertEqual(4, obj.minMeetingRooms(self.meetings_2))
