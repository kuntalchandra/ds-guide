"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.



Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Alternative: Given an integer array nums, find the largest sum of any contiguous subarray
Kadane's algorithm

Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    """
    def maxSubArray(self, nums: List[int]) -> int:
        temp = total = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], temp + nums[i])
            total = max(total, temp)
        return total
    """

    def maxSubArray(self, nums: List[int]) -> int:
        """
        [Wikipedia] This version of the algorithm will return 0 if the input contains no positive elements, including when the
        input is empty. For the variant of the problem which disallows empty subarrays, best_sum should be initialized
        to negative infinity instead[11] and also in the for loop current_sum should be updated as
        max(x, current_sum + x).[note 6] In that case, if the input contains no positive element, the returned value is
        that of the largest element (i.e., the least negative value), or negative infinity if the input was empty.
        """
        if not nums:
            return 0
        max_sum, current_sum = 0, 0

        for i in nums:
            current_sum = max(0, current_sum + i)
            max_sum = max(max_sum, current_sum)
        return max_sum
