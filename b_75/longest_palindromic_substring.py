"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        sub_str = ""

        for left in range(length):
            for right in range(length, left, -1):
                if len(sub_str) >= (right - left):
                    break
                if s[left:right] == s[left:right][::-1]:
                    sub_str = s[left:right]
                    break
        return sub_str
