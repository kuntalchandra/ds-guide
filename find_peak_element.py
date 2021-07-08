"""
Find peak element
Alternative: Peak index in mountain array

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return
the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the
peak element is 6.

Follow up: You must write an algorithm that runs in O(log n) time.
"""
from typing import List


class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        length = len(nums)
        if length <= 1:
            return 0
        right = length - 1

        while right > 1 and nums[right - 1] > nums[right]:
            right -= 1

        if nums[right - 1] < nums[right]:
            return right
        return 0

    def findPeakElement(self, nums: List[int]) -> int:
        """
        Time complexity: O(logn)
        Space complexity: O(1)
        """
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
