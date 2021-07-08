"""
Search for a range

Find the first and last position of k

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        if not nums:
            return [start, end]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            start = left
            left += 1
            right = len(nums) - 1
        else:
            return [start, end]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            else:
                right = mid
        if nums[right] == target:
            end = right
        else:
            end = right - 1
        return [start, end]
