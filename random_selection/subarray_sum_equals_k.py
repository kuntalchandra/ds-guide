"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = {0: 1}
        counter, curr_sum = 0, 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in cumulative_sum:
                counter += cumulative_sum[diff]

            if curr_sum in cumulative_sum:
                cumulative_sum[curr_sum] += 1
            else:
                cumulative_sum[curr_sum] = 1

        return counter
