"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time and Space: O(n), O(n)
        """
        if not nums:
            return 0
        lcs, seq_len = 1, 0
        nums_set = set(nums)
        for idx, num in enumerate(nums):
            if num - 1 not in nums_set:
                seq_len = 1
                while num + 1 in nums_set:
                    seq_len += 1
                    num += 1
            lcs = max(lcs, seq_len)
        return lcs
