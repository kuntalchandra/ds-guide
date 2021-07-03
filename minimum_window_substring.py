"""
Minimum Window Substring

TODO: Followup

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in
complexity O(n).
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
Approach:
Use a simple sliding window approach to solve this problem.
In any sliding window based problem we have two pointers. One rightright pointer whose job is to expand the current
window and then we have the leftleft pointer whose job is to contract a given window. At any point in time only one of
these pointers move and the other one remains fixed.
The solution is pretty intuitive. We keep expanding the window by moving the right pointer. When the window has all the
desired characters, we contract (if possible) and save the smallest window till now.
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import Counter
from unittest import TestCase


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        if s == t:
            return s
        required = Counter(t)
        required_count = len(required.keys())
        start = end = 0
        left = right = -1
        length = len(s)
        while True:
            if start <= end and end < length and required_count > 0:  # Expand
                char = s[end]
                if char in required:
                    required[char] -= 1
                    if required[char] == 0:
                        required_count -= 1
                end += 1
            elif start <= end and required_count == 0:  # Shrink
                char = s[start]
                if left == -1 or (end - start) < (right - left):
                    left, right = start, end
                if char in required:
                    required[char] += 1
                    if required[char] == 1:
                        required_count += 1
                start += 1
            else:
                break
        if left == -1:
            return ""
        else:
            return s[left:right]


class TestMinWindow(TestCase):
    def setUp(self) -> None:
        self.s_1 = "ADOBECODEBANC"
        self.t_1 = "ABC"
        self.s_2 = "a"
        self.t_2 = "aa"
        self.s_3 = "ab"
        self.t_3 = "a"
        self.s_4 = "bba"
        self.t_4 = "ab"

    def test_min_window(self) -> None:
        obj = Solution()
        self.assertEqual("BANC", obj.minWindow(self.s_1, self.t_1))
        self.assertEqual("", obj.minWindow(self.s_2, self.t_2))
        self.assertEqual("a", obj.minWindow(self.s_3, self.t_3))
        self.assertEqual("ba", obj.minWindow(self.s_4, self.t_4))
