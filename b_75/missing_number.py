"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array
Example 1:
Input: [3,0,1]
Output: 2
Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space
complexity
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        O(n), O(n)
        """
        nums_set = set(nums)
        for idx, _ in enumerate(nums_set):
            if idx not in nums_set:
                return idx
        return len(nums)

    def missingNumberOptimised(self, nums) -> int:
        """
        Gauss' Formulą
        O(n), O(1)
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
