"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        for c, cnt in s_cnt.items():
            if c not in t_cnt or s_cnt[c] != t_cnt[c]:
                return False
        return True
