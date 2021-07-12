"""
Minimum Increment to Make Array Unique

Given an array of integers nums, a move consists of choosing any nums[i], and incrementing it by 1.

Return the least number of moves to make every value in nums unique.



Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:  # [3,2,1,2,1,7]
        level = -1
        res = 0
        nums.sort()  # [1, 1, 2, 2, 3, 7]

        for num in nums:  # 1, 1, 2, 2, 3, 7
            if level < num:
                level = num  # 1, 7
            else:
                level += 1  # 2, 3, 4, 5
                res += level - num  # 1, 2, 4, 6
        return res
