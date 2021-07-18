"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_arr, right_arr = [0] * length, [0] * length
        left_arr[0] = 1
        for i in range(1, length):  # from 1 -> n
            left_arr[i] = nums[i - 1] * left_arr[i - 1]

        right_arr[-1] = 1
        for i in range(length - 2, -1, -1):  # from n - 2 -> 0
            right_arr[i] = nums[i + 1] * right_arr[i + 1]

        res = []
        for i in range(length):
            res.append(left_arr[i] * right_arr[i])

        return res
