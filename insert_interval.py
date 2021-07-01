"""
Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        i, j, n = 0, 0, len(intervals)

        while i < n and newInterval[0] > intervals[i][1]:
            i += 1

        j = i
        while j < n and newInterval[1] >= intervals[j][0]:
            j += 1

        if i == j:
            result = newInterval
        else:
            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[j - 1][1])
            result = [start, end]

        return intervals[:i] + [result] + intervals[j:]


class TestIntervals(TestCase):
    def setUp(self):
        self.intervals_1 = [[1, 3], [6, 9]]
        self.new_interval_1 = [2, 5]
        self.intervals_2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        self.new_interval_2 = [4, 8]

    def test_insert_interval(self) -> None:
        interval_insert = Solution()
        self.assertListEqual([[1, 5], [6, 9]], interval_insert.insert(self.intervals_1, self.new_interval_1))
        self.assertListEqual([[1, 2], [3, 10], [12, 16]], interval_insert.insert(self.intervals_2, self.new_interval_2))
