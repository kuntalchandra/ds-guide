"""
Calculate the maximum possible vacation Length.

[
Similar variation of Max Consecutive Ones III
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
]

Given boolean array year at office [T, F, T, T, F, F, F, T] and PTO an integer, calculate the maximum possible vacation
length. Here, the boolean True means company holiday and False indicates an employee can take a paid time off. Find the
maximum length of vacation an employee can take.

Example 1:
Input: year = [False, True, False, True, False, True, False], pto: 2
Output: 5
Explanation: Taking off on year[2] and year[5] provides the longest vacation window of consecutive 5 days.

Example 2:
Input: year = [False, True, False], pto = 1
Output: 2

Example 3:
Input: year = [False, True, False], pto = 0
Output: 1

Example 4:
Input: year = [True, True, True, False, False, False, True, True, True, True, False], pto = 2
Output: 6

Approach:
Initialize two pointers. The two pointers will help to mark the left and right end of the window with contiguous 1's.
left = 0, right = 0, window_size = 0
Use the right pointer to expand the window until the window is desirable. i.e. number of 0's in the window are in the
allowed range of [0, K].
Once get a window which has more than the allowed number of 0's, move the left pointer ahead one by one until encounter
0 on the left too. This step ensures to throw out the extra zero.

Visual credit: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/719833/python3-sliding-window-with-clear-example-explains-why-the-soln-works
"""
from typing import List
from unittest import TestCase


def max_holidays(year: List[bool], pto: int) -> int:
    if not year:
        return 0
    left = 0
    # iterate all the days
    for right in range(len(year)):
        # if it's not a holiday, consider taking a pto, otherwise no impact on pto
        if not year[right]:
            pto -= 1

        # pto exhausted, increase left pointer to reconsider the earlier pto
        if pto < 0:
            # if pto was considered at the beginning of the window
            if not year[left]:
                # increase considered pto
                pto += 1
            # if pto is exhausted, increment the pointer irrespective of holiday or pto
            left += 1
    return right - left + 1


class TestMaxHolidays(TestCase):
    def setUp(self) -> None:
        self.year_1 = [False, True, False, True, False, True, False]
        self.pto_1 = 2
        self.year_2 = [False, True, False]
        self.pto_2 = 1
        self.year_3 = [False, True, False]
        self.pto_3 = 0
        self.year_4 = [True, True, True, False, False, False, True, True, True, True, False]
        self.pto_4 = 2

    def test_max_holidays(self) -> None:
        self.assertEqual(5, max_holidays(self.year_1, self.pto_1))
        self.assertEqual(2, max_holidays(self.year_2, self.pto_2))
        self.assertEqual(1, max_holidays(self.year_3, self.pto_3))
        self.assertEqual(6, max_holidays(self.year_4, self.pto_4))
