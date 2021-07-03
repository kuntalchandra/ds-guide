"""
Longest Substring Without Repeating Characters
Time complexity: O(n^2)
Space complexity: O(n)
"""
from unittest import TestCase


class Solution(object):
    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = []
        max_length = 0

        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x) + 1:]

            str_list.append(x)
            max_length = max(max_length, len(str_list))
        return max_length


class TestLengthOfLongestSubstring(TestCase):
    def setUp(self):
        self.obj = Solution()
        self.input_s_1 = "abcabcbb"
        self.input_s_2 = "bbbbb"
        self.input_s_3 = "pwwkew"
        self.input_s_4 = "dvdf"

    def test_length_of_longest_substring(self):
        self.assertEqual(3, self.obj.length_of_longest_substring(self.input_s_1))
        self.assertEqual(1, self.obj.length_of_longest_substring(self.input_s_2))
        self.assertEqual(3, self.obj.length_of_longest_substring(self.input_s_3))
        self.assertEqual(3, self.obj.length_of_longest_substring(self.input_s_4))
