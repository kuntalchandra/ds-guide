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
        length = len(s)
        max_s = ""
        for left in range(length):  # O(n)
            for right in range(length, left, -1):   # O(n)
                if right - left < len(max_s):
                    break
                if s[left:right] == s[left:right][::-1]:    # O(n)
                    max_s = s[left:right]
                    break
        return max_s


class TestLongestPalindrome(TestCase):
    def setUp(self) -> None:
        self.s_1 = "abace"
        self.s_2 = "a"

    def test_longest_palindrome(self):
        obj = Solution()
        self.assertEqual("aba", obj.longestPalindrome(self.s_1))
        self.assertEqual("a", obj.longestPalindrome(self.s_2))
