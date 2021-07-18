"""
4 Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""


class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i == 0 or nums[i] != nums[i - 1]:
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[left], nums[right]])
                        # de-duplication
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                temp = self.threeSum(nums[i + 1:], target - nums[i])
                for item in temp:
                    res.append([nums[i]] + item)
        return res
