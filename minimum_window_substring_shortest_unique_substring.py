"""
Minimum Window Substring

TODO: Followup

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in
complexity O(n).
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
Approach:
Use a simple sliding window approach to solve this problem.
In any sliding window based problem we have two pointers. One rightright pointer whose job is to expand the current
window and then we have the leftleft pointer whose job is to contract a given window. At any point in time only one of
these pointers move and the other one remains fixed.
The solution is pretty intuitive. We keep expanding the window by moving the right pointer. When the window has all the
desired characters, we contract (if possible) and save the smallest window till now.
Time complexity: O(n)
Space complexity: O(n)

Similar Variation:

Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds
the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring
does not exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
"""
from collections import Counter
from unittest import TestCase


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        if s == t:
            return s
        required = Counter(t)
        required_count = len(required.keys())
        start = end = 0
        left = right = -1
        length = len(s)
        while True:
            if start <= end and end < length and required_count > 0:  # Expand
                char = s[end]
                if char in required:
                    required[char] -= 1
                    if required[char] == 0:
                        required_count -= 1
                end += 1
            elif start <= end and required_count == 0:  # Shrink
                char = s[start]
                if left == -1 or (end - start) < (right - left):
                    left, right = start, end
                if char in required:
                    required[char] += 1
                    if required[char] == 1:
                        required_count += 1
                start += 1
            else:
                break
        if left == -1:
            return ""
        else:
            return s[left:right]


def get_shortest_unique_substring(arr, source_str):
    start, end, length, unique_count = 0, 0, len(source_str), 0
    res = ""
    # count map
    count_map = {c: 0 for c in arr}

    # build the sub_str until it contains all unique char from array
    for end in range(length):  # 0, 1, 2, 3, 4, 5, 6, 7
        # handle the new end
        end_c = source_str[end]  # x, y, y, z, y, z, y, x

        # skip current char if not in count map
        if end_c not in count_map:
            continue

        if count_map[end_c] == 0:
            unique_count += 1  # 1, 2, 3, 3
        count_map[end_c] += 1  # {x: 1, y: 1, y: 2, z: 1, y: 3, z: 2, y: 4, x: 1}

        while unique_count == len(arr):  # 3 == 3, 2 != 3, 3 == 3
            temp_length = (end - start) + 1  # 4, 6

            # it can't be shorter than this
            if temp_length == len(arr):
                return source_str[start: end + 1]

            # keep building a valid substring which meets the requirement till now
            if not res or temp_length < len(res):
                # found sub_str till now
                res = source_str[start: end + 1]  # xyyz,

            start_c = source_str[start]  # x, y
            if start_c in count_map:
                start_count = count_map[start_c] - 1  # 0, 4
                if start_count == 0:
                    unique_count -= 1  # 2
                count_map[start_c] = start_count  # {x: 0}

            start += 1  # 1
    return res


class TestMinWindow(TestCase):
    def setUp(self) -> None:
        self.s_1 = "ADOBECODEBANC"
        self.t_1 = "ABC"
        self.s_2 = "a"
        self.t_2 = "aa"
        self.s_3 = "ab"
        self.t_3 = "a"
        self.s_4 = "bba"
        self.t_4 = "ab"

    def test_min_window(self) -> None:
        obj = Solution()
        self.assertEqual("BANC", obj.minWindow(self.s_1, self.t_1))
        self.assertEqual("", obj.minWindow(self.s_2, self.t_2))
        self.assertEqual("a", obj.minWindow(self.s_3, self.t_3))
        self.assertEqual("ba", obj.minWindow(self.s_4, self.t_4))
