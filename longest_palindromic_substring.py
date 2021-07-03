"""
Longest Palindromic Substring
"""

from unittest import TestCase


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time complexity: O(n^2)
        """
        if len(s) == 1:
            return s
        res = ""
        for i in range(len(s)):
            # Odd s "aba"
            odd = self.find_palindrome(i, i, s)
            # even s "abba"
            even = self.find_palindrome(i, i + 1, s)
            res = max(res, odd, even, key=len)
        return res

    def find_palindrome(self, left: int, right: int, s: str) -> str:
        # Expand from inner to outer
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def longestPalindrome1(self, s: str) -> str:
        """
        Time complexity: O(n^3)
        """
        m = ""
        for i in range(len(s)):  # i = start, O(n)
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:  # O(n)
                    m = s[i:j]
                    break
        return m


class TestLongestPalindrome(TestCase):
    def setUp(self) -> None:
        self.s_1 = "abace"
        self.s_2 = "a"

    def test_longest_palindrome(self):
        obj = Solution()
        self.assertEqual("aba", obj.longestPalindrome(self.s_1))
        self.assertEqual("a", obj.longestPalindrome(self.s_2))
