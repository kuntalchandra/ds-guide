"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for
which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Approach:
Monotonic decreasing stack of indices — "pending questions waiting for a warmer day."
For each day, while current temp > temp at stack top, that index has its answer.
Pop it, compute days_waited = current_index - popped_index.

stack = []          # indices of unresolved days
result = [0] * len(temperatures)

for current_idx, temp in enumerate(temperatures):
    while stack and temperatures[stack[-1]] < temp:
        prev_idx = stack.pop()
        result[prev_idx] = current_idx - prev_idx
    stack.append(current_idx)

return result

Triggers:
- "next greater element" in any form
- each element is waiting to find something larger/smaller ahead of it
- answer for index i depends on a future element

Variants / Watch-outs:
- Next Greater Element II (circular array): iterate 2 * len(nums), use index % n
- Largest Rectangle in Histogram: pop when current bar is shorter, compute area using popped index
- Stack stores INDICES not values — you need the position to compute the distance
"""
from typing import List
from unittest import TestCase


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialise with 0s considering no bigger temperature
        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            # check if current temp is greater than the last appended stack value. Pop all the lesser elements
            while stack and stack[-1][1] < temp:
                index, value = stack.pop()
                # Check how many days are passed since the lesser temp
                ans[index] = idx - index
                # There is comparison for all the stack elements before inserting,
                # So, all the stack elements will have temperatures greater than the current one
            stack.append([idx, temp])

        return ans


class TestFinal(TestCase):
    def setUp(self) -> None:
        self.temperatures_1 = [73, 74, 75, 71, 69, 72, 76, 73]

    def test_daily_temperatures(self) -> None:
        obj = Solution()
        self.assertListEqual([1, 1, 4, 2, 1, 1, 0, 0], obj.dailyTemperatures(self.temperatures_1))
