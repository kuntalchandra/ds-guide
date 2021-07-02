"""
House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
Input: [2,3,2]
Output: 3
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Runtime: 32 ms, faster than 60.42%
        O(n), O(1)
        """
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums: List[int]) -> int:
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)


class TestHouseRobber(TestCase):
    def setUp(self) -> None:
        self.nums_1 = [2, 3, 2]
        self.nums_2 = [1, 2, 3, 1]
        self.nums_3 = [0]
        self.nums_4 = [2, 1, 1, 2]
        self.nums_5 = [1, 2, 1, 1]

    def test_rob(self) -> None:
        obj = Solution()
        self.assertEqual(3, obj.rob(self.nums_1))
        self.assertEqual(4, obj.rob(self.nums_2))
        self.assertEqual(0, obj.rob(self.nums_3))
        self.assertEqual(3, obj.rob(self.nums_4))
        self.assertEqual(3, obj.rob(self.nums_5))
