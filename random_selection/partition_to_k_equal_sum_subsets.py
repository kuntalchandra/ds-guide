"""
Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty
subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        O(k * 2^n) time complexity when starting from each subset.
        Alternatively, (not implemented) starting from each number that could be with O(n * 2^k) time complexity
        """
        if len(nums) < k:
            return False
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        sub_sum = total_sum // k
        # keep the bigger numbers in front and if the answer is true, will save time to group smaller numbers
        # small numbers can be placed into more groups than the bigger numbers
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        return self.can_partition(k, 0, 0, sub_sum, visited, nums)

    def can_partition(self, remaining_k: int, curr_sum: int, next_idx: int, sub_sum: int, visited: List[bool],
                      nums: List[int]) -> bool:
        # if k - 1 groups are found then remaining last group must be the target sum
        if remaining_k == 1:
            return True
        if curr_sum == sub_sum:
            return self.can_partition(remaining_k - 1, 0, 0, sub_sum, visited, nums)
        for i in range(next_idx, len(nums)):
            if not visited[i] and curr_sum + nums[i] <= sub_sum:
                visited[i] = True
                if self.can_partition(remaining_k, curr_sum + nums[i], next_idx + 1, sub_sum, visited, nums):
                    return True
                visited[i] = False
        return False
