"""
Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer
with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
Worth read: https://leetcode.com/problems/perfect-squares/solution/
"""
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        sq_nums = [i ** i for i in range((n // 2) + 1)]
        q = deque([n])
        level = 0
        while q:
            level += 1
            # use set() instead of list() to eliminate the redundancy, leads to 5-times speedup, 200ms vs. 1000ms.
            next_q = set()
            # construct the queue for the next level
            for remain in q:
                for sq_num in sq_nums:
                    if remain == sq_num:
                        # found the node
                        return level
                    elif remain < sq_num:
                        break
                    else:
                        next_q.add(remain - sq_num)
            q = next_q
        return level
