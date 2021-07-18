"""
Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
from unittest import TestCase


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.backtrack(s, {})

    def backtrack(self, s: str, memo: dict) -> int:
        if not s:
            return 1
        if s in memo:
            return memo[s]
        consider_one, consider_two = 0, 0
        if int(s[:1]) >= 1 and int(s[:1]) <= 9:
            consider_one = self.backtrack(s[1:], memo)
        if int(s[:2]) >= 10 and int(s[:2]) <= 26:
            consider_two = self.backtrack(s[2:], memo)
        memo[s] = consider_one + consider_two
        return memo[s]


class TestDecodeWays(TestCase):
    def setUp(self) -> None:
        self.s_1 = "12"

    def test_decode_ways(self) -> None:
        obj = Solution()
        self.assertEqual(2, obj.numDecodings(self.s_1))
