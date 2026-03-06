"""
Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
Time complexity: O(n)
Space complexity: O(1)


Approach:
Three phases in one pass — no sort needed (already sorted):
Phase 1: collect all intervals that END before new interval starts (no overlap).
Phase 2: merge all intervals that OVERLAP with new interval (update new interval's bounds).
Phase 3: append remaining intervals untouched.

left_idx = 0
while left_idx < len(intervals) and new_interval[0] > intervals[left_idx][1]:
    left_idx += 1                           # phase 1: before new interval

right_idx = left_idx
while right_idx < len(intervals) and new_interval[1] >= intervals[right_idx][0]:
    right_idx += 1                          # phase 2: overlapping, absorb them

if left_idx == right_idx:
    merged = new_interval
else:
    merged = [min(new_interval[0], intervals[left_idx][0]),
              max(new_interval[1], intervals[right_idx - 1][1])]

return intervals[:left_idx] + [merged] + intervals[right_idx:]

Time: O(n) — already sorted, single pass
Space: O(n) output

Triggers:
- insert into an already-sorted interval list
- "add a new booking/event, merge if needed"
- O(n) when input is pre-sorted vs O(n log n) for unsorted

Variants / Watch-outs:
- Optimisation angle: if interviewer says "what if input is not sorted?" — binary search
  for insertion point O(log n) to find left boundary, then linear merge
- Watch the phase boundaries: >  vs >= matters for touching-but-not-overlapping edges
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
