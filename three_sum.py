"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Time Complexity: twoSumII O(n), and call it n times. Sorting the array takes O(nlogn), so overall complexity is O(n^2)
Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm.

Follow up: 3Sum Smaller
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with
0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target

Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0


Follow up: 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 3 and sum(nums) == 0:
            return [[nums[0], nums[1], nums[2]]]
        nums.sort()
        triplets = set()
        length = len(nums)

        for i in range(length):
            left = i + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return [list(t) for t in triplets]

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        count = 0
        nums.sort()
        length = len(nums)

        for i in range(length):
            left, right = i + 1, length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # if (i + left + right) works then (i + left + right - 1), (i + left + 1, right) =>
                # all falling within the range will fit in
                if total < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        closest = sum(nums[:3])

        for i in range(length):
            left, right = i + 1, length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - closest):
                    closest = total
                if closest == target:
                    return closest
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return closest
