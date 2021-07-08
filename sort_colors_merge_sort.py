"""
Sort colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's
and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Merge sort: O(nLogn), O(n)
        """
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            self.sortColors(left)
            self.sortColors(right)

            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1

            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1

    def sort_colors_optimised(self, nums: List[int]) -> None:
        """
        Counting sort approach: O(n+k), O(k)
        """
        max_len = 2 + 1  # max_value + 1
        counter = [0] * max_len
        for i in nums:
            counter[i] += 1  # Keep count at its index

        i = 0
        for j in range(max_len):  # Iterate each counted values
            for c_idx in range(counter[j]):  # 0 => Count
                nums[i] = j
                i += 1
