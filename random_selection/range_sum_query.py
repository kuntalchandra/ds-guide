"""
Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # O(n) space to store precomputed sum
        self.computed_sum = [0] * (len(nums) + 1)
        self.pre_compute()

    # O(n) times complexity to precompute
    def pre_compute(self) -> None:
        for idx, num in enumerate(self.nums):
            self.computed_sum[idx + 1] = self.computed_sum[idx] + num

    # O(1) time complexity to get the query result
    def sumRange(self, left: int, right: int) -> int:
        # slower as every single time computes
        # return sum(self.nums[left: right + 1])
        return self.computed_sum[right + 1] - self.computed_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
