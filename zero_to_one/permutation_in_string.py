"""
Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ord_s1 = [ord(x) - ord('a') for x in s1]
        ord_s2 = [ord(x) - ord('a') for x in s2]
        target = [0] * 26
        for x in ord_s1:
            target[x] += 1
        window = [0] * 26
        for idx, v in enumerate(ord_s2):
            window[v] += 1
            if idx >= len(ord_s1):
                window[ord_s2[idx - len(ord_s1)]] -= 1
            if window == target:
                return True
        return False
