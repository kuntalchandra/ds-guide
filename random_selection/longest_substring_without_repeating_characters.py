"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, max_idx = 0, 0
        char_map = {}
        for idx in range(len(s)):
            if s[idx] in char_map:
                max_idx = max(char_map[s[idx]], max_idx)
            max_len = max(max_len, (idx - max_idx) + 1)
            char_map[s[idx]] = idx + 1
        return max_len
    
    def lengthOfLongestSubstring1(self, s: str) -> int:
        sub_str = []
        max_len = 0
        # O(n) to iterate each char then O(n) to lookup in sub_str => O(n^2)
        for c in s:
            if c in sub_str:
                sub_str = sub_str[sub_str.index(c) + 1:]
            sub_str.append(c)
            max_len = max(max_len, len(sub_str))
        return max_len
