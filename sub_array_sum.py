"""
Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals to k
Approach-
Calculate cumulative sum and store in hashmap. If there is a increase of k, then that's a subarray.
Consider the difference between 0 to k in the c_sum by addressing {0: 1}
Time complexity: O(n)
Spce complexity: O(n)
"""
from typing import List
from unittest import TestCase


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c_sum = dict()
        c_sum[0] = 1
        counter = 0
        sum_ = 0
        for i in nums:
            sum_ += i
            counter += c_sum.get(sum_ - k, 0)
            c_sum[sum_] = c_sum.get(sum_, 0) + 1
        return counter


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.nums_1 = [1, 1, 1]
        self.k_1 = 2
        self.nums_2 = [1, 2, 3]
        self.k_2 = 3
        self.nums_3 = [1, 2, 1, 2, 1]
        self.k_3 = 3

    def testSubarraySum(self) -> None:
        obj = Solution()
        self.assertEqual(2, obj.subarraySum(self.nums_1, self.k_1))
        self.assertEqual(2, obj.subarraySum(self.nums_2, self.k_2))
        self.assertEqual(4, obj.subarraySum(self.nums_3, self.k_3))
