"""
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""
from typing import List


class Solution:
    def sortedSquares_nlogn(self, nums: List[int]) -> List[int]:
        squares = []
        for num in nums:
            squares.append(num * num)
        return sorted(squares)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            l, r = abs(nums[left]), abs(nums[right])
            if l > r:
                squares[right - left] = l * l
                left += 1
            else:
                squares[right - left] = r * r
                right -= 1
        return squares
