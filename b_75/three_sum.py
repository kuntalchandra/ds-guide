"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

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

Time Complexity: O(n^2). two Sum O(n). Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n^2).
This is asymptotically equivalent to O(n^2).
Space Complexity: O(n)

Detailed mental model:
Sort first — this is what makes two-pointer viable and duplicate-skipping trivial.
Fix one element with outer loop. For the remaining two, run two pointers from both ends.

nums.sort()
for idx, value in enumerate(nums):
    if idx > 0 and nums[idx] == nums[idx - 1]: continue   # skip outer dup

    left, right = idx + 1, len(nums) - 1
    while left < right:
        total = value + nums[left] + nums[right]
        if total == 0:
            result.append([value, nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]: left += 1
            while left < right and nums[right] == nums[right - 1]: right -= 1
            left += 1; right -= 1
        elif total < 0: left += 1
        else: right -= 1

Triggers:
- triplets summing to 0 (or any target)
- "all unique combinations" — content matters, not indices
- you see "no duplicate triplets" in constraints

Variants / Watch-outs:
- k-sum: fix k-2 elements recursively, two-pointer at the bottom level
- Closest 3Sum: track abs(total - target) instead of checking == 0
- Duplicate skipping is the #1 mistake — skip AFTER collecting, at BOTH levels
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        elif length == 3 and sum(nums) == 0:
            return [nums]
        nums.sort()

        res = set()
        for i in range(length):
            left = i + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in res]