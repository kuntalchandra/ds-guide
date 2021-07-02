"""
House Robber I
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4
Approach: Top down DP --> Start at the first house, end at last house
Time complexity: O(n), O(n)
Space complexity: O(n), O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)


class TestRob(TestCase):
    def setUp(self) -> None:
        self.nums_1 = [1, 2, 3, 1]
        self.nums_2 = [2, 7, 9, 3, 1]
        self.nums_3 = [0]
        self.nums_4 = [2, 1, 1, 2]
        self.nums_5 = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128,
                       177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]

    def test_rob(self) -> None:
        obj = Solution()
        self.assertEqual(4, obj.rob(self.nums_1))
        self.assertEqual(12, obj.rob(self.nums_2))
        self.assertEqual(0, obj.rob(self.nums_3))
        self.assertEqual(4, obj.rob(self.nums_4))
        self.assertEqual(3365, obj.rob(self.nums_5))
