"""
Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose
elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Approach:
If k == 0, search for any consecutive pair of 0s
Otherwise, keep track of indices using cumulative sum i.e. prefix sum modulo by k. If that result can be seen
at least 2 indices before, then it matches the conditions. subarray that has a sum(subarray) % k == 0 and that
subarray has at least 2 elements.
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        mods, cumm_sum_mod_k = {0: -1}, 0
        for idx, num in enumerate(nums):
            cumm_sum_mod_k = (cumm_sum_mod_k + num) % k
            if cumm_sum_mod_k in mods and idx - mods[cumm_sum_mod_k] > 1:
                return True
            if cumm_sum_mod_k not in mods:
                mods[cumm_sum_mod_k] = idx
        return False
