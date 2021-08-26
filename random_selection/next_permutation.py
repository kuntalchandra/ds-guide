"""
Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending
order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]

Time complexity; O(n)
Space complexity: O(1)
Question explained: Think of the list of numbers as a single integer. For example, think of [1,3,7,3,2] as 13732.
The goal is to create the next highest number, using only the same digits. The next biggest number is 17233
Approach: Next lexicographical permutation algorithm
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. find the longest desc sub series
        right = len(nums) - 1
        while right > 0 and nums[right - 1] >= nums[right]:
            right -= 1

        # 2. if starts from 0, reverse the entire series
        if right == 0:
            nums = self.reverse(0, len(nums) - 1, nums)
            return

            # 3. find the pivot = last asc element before the sub series
        pivot = right - 1
        k = 0

        # 4. swap position = rightmost successor of pivot
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                k = i
                break

        # 5. swap the pivot and the successor
        nums[k], nums[pivot] = nums[pivot], nums[k]

        # 6. reverse the subseries
        nums = self.reverse(pivot + 1, len(nums) - 1, nums)

    def reverse(self, left: int, right: int, nums: List[int]) -> List[int]:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
