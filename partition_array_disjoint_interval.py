"""
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
"""
from typing import List
from unittest import TestCase


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:  # [5, 0, 3, 8, 6]
        if not nums:
            return 0
        length = len(nums)
        max_left = [0] * length
        min_right = [0] * length

        max_num = nums[0]
        for i in range(length):  # 5, 0, 3, 8, 6
            max_num = max(max_num, nums[i])  # 5, 5, 5, 8, 8
            max_left[i] = max_num  # [5, 5, 5, 8, 8]

        min_num = nums[-1]
        for i in range(length - 1, -1, -1):  # 6, 8, 3, 0, 5
            min_num = min(min_num, nums[i])  # 6, 6, 3, 0, 0
            min_right[i] = min_num          # [0, 0, 3, 6, 6]

        for i in range(1, length):
            if max_left[i - 1] <= min_right[i]:
                return i


class TestPartition(TestCase):
    def setUp(self) -> None:
        self.nums = [5, 0, 3, 8, 6]

    def test_partition(self):
        obj = Solution()
        self.assertEqual(3, obj.partitionDisjoint(self.nums))
