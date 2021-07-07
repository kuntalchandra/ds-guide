"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Approach:
Backtracking is a complete search technique and BFS is an ideal way to implement it.
Time complexity: O(n * n!)
Space complexity: O(n * n!)
"""
from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        q = deque()
        q.append(([], nums))

        while q:
            arr, options = q.popleft()

            for i in range(len(options)):
                remaining_options = options[:i] + options[i + 1:]
                tmp_arr = arr + [options[i]]

                if remaining_options:
                    q.append((tmp_arr, remaining_options))
                else:
                    res.append(tmp_arr)
        return res
