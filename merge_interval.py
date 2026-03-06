"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.



Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Similar variant of interval scheduling-
Non-overlapping Intervals

Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals you
need to remove to make the rest of the intervals non-overlapping.


Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Approach:
Sort by start time. Walk linearly, comparing each interval to the
LAST interval in the result list. If they overlap, extend the last
interval's end. If not, append as new interval.

intervals.sort(key=lambda interval: interval[0])
result = []
for start, end in intervals:
    if not result or start > result[-1][1]:
        result.append([start, end])         # no overlap, new interval
    else:
        result[-1][1] = max(result[-1][1], end)  # overlap, extend end

Time: O(n log n)
Space: O(n) output

Triggers:
- merge all overlapping intervals
- reduce a set of ranges to disjoint intervals
- preprocessing step before interval queries

Variants / Watch-outs:
- Optimisation angle: common mistake is merging eagerly without sorting first — O(n²)
- Non-Overlapping Intervals (min removals): sort by END time (not start), greedily keep
  intervals with earliest end — identical structure, different sort key
- Watch: max(result[-1][1], end) not just end — current interval could be fully contained
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]
        intervals.sort(key=lambda n: n[0])
        res = []
        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(end, res[-1][1])
        return res

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda n: n[0])
        _, end = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start < end:
                count += 1
                end = min(curr_end, end)
            else:
                end = curr_end
        return count

