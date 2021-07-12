"""
Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No
two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""
from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        source_cnt = Counter(s)
        target_cnt = Counter(t)
        if len(source_cnt.values()) != len(target_cnt.values()):
            return False
        maps = {}
        for i, c in enumerate(s):
            if c in maps and maps[c] != t[i]:
                return False
            maps[c] = t[i]

        return True
