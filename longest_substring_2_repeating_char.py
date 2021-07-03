"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Note: Implemented using k distinct which answers longest substring with k distinct characters.
Note2: Variation of fruit into basket

Time complexity: O(n) where N is a number of characters in the input string
Space complexity: O(1) since additional space is used only for a hashmap with at most 3 elements
"""
from collections import defaultdict
from unittest import TestCase


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) < 3:
            return len(s)
        left = right = 0
        max_len = 2
        k = 2
        hashmap = defaultdict(int)

        while right < len(s):
            if len(hashmap) < 3:
                hashmap[s[right]] += 1
                right += 1
            while len(hashmap) > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            max_len = max(max_len, right - left)
        return max_len


class TestLongestSubstring(TestCase):
    def setUp(self) -> None:
        self.s_1 = "eceba"
        self.s_2 = "ccaabbb"
        self.s_3 = "cdaba"

    def test_longest_substring(self) -> None:
        obj = Solution()
        self.assertEqual(3, obj.lengthOfLongestSubstringTwoDistinct(self.s_1))
        self.assertEqual(5, obj.lengthOfLongestSubstringTwoDistinct(self.s_2))
        self.assertEqual(3, obj.lengthOfLongestSubstringTwoDistinct(self.s_3))