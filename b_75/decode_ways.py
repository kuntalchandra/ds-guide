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

Approach:
At each position: take 1 digit (valid unless it's '0') OR take 2 digits
(valid only if the two-digit value is 10-26). Memoized recursion or iterate forward.
'0' always kills the single-digit choice — return 0 immediately for that branch.

dp = {len(s): 1}    # empty suffix = exactly 1 way

for idx in range(len(s) - 1, -1, -1):
    if s[idx] == '0':
        dp[idx] = 0
    else:
        dp[idx] = dp[idx + 1]                           # take 1 digit
        if idx + 1 < len(s) and int(s[idx:idx + 2]) <= 26:
            dp[idx] += dp[idx + 2]                      # take 2 digits

return dp[0]

Triggers:
- count decodings of a numeric string
- at each position, 1 or 2 choices with validity constraints
- overlapping subproblems on string suffixes

Variants / Watch-outs:
- '0' alone = 0 ways; '10' or '20' = valid 2-digit; '30' = invalid 2-digit
- With '*' wildcard: multiply by number of valid single/double interpretations of '*'
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
