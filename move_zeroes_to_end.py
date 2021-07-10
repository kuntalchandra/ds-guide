"""
Move zeroes to the end
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements. Must be in-place with minimum pass.
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if not length:
            return []
        non_zero = 0
        for cur in range(length):
            if nums[cur]:
                nums[cur], nums[non_zero] = nums[non_zero], nums[cur]
                non_zero += 1
        return nums


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.nums_1 = [0, 1, 0, 3, 12]

    def test_move_zeroes(self) -> None:
        obj = Solution()
        self.assertListEqual([1, 3, 12, 0, 0], obj.moveZeroes(self.nums_1))
