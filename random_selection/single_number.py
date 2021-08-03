"""
Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR of 0 and some bit => some bit
        XOR of two same bits => 0
        XOR all bits together to find the unique number
        Space: O(1)
        """
        a = 0
        for num in nums:
            a ^= num
        return a

    def singleNumber1(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, frequency in count.items():
            if frequency == 1:
                return num
