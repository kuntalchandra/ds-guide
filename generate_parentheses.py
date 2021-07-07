"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Approach: Backtracking
Time complexity: O(4^n/sqrt(n)). Each valid sequence has at most n steps during the backtracking procedure.
Space complexity: O(4^n/sqrt(n)), as described above, and using O(n) space to store the sequence.
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return ""
        return self.helper([], "", 0, 0, n)

    def helper(self, arr: List[str], braces: str, open_: int, close_: int, max_: int) -> List[str]:
        if len(braces) == max_ * 2:
            arr.append(braces)
        if open_ < max_:
            self.helper(arr, braces + "(", open_ + 1, close_, max_)
        if close_ < open_:
            self.helper(arr, braces + ")", open_, close_ + 1, max_)
        return arr
