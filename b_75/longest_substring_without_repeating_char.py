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


Approach:
Sliding window. Valid window condition: (window_length - count_of_most_frequent_char) <= k.
Same "window only grows" trick as max_holidays — never truly shrink, slide by 1 when invalid.
max_freq only ever increases — you only care about beating the best window seen so far.

char_count = {}
max_freq = 0
left = 0

for right, ch in enumerate(s):
    char_count[ch] = char_count.get(ch, 0) + 1
    max_freq = max(max_freq, char_count[ch])

    if (right - left + 1) - max_freq > k:      # window invalid
        char_count[s[left]] -= 1
        left += 1                               # slide by exactly 1

return right - left + 1

Triggers:
- longest substring after at most k character replacements
- "window_size - dominant_frequency <= k" is the validity condition
- max_freq never decrements — this is intentional, tracks historical best

Variants / Watch-outs:
- max_freq intentionally not decremented on shrink — the window only needs to grow
- Same skeleton as Max Consecutive Ones III — recognizing the family is the skill

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        max_len = 0
        for c in s:
            if c in res:
                res = res[res.index(c) + 1:]
            res.append(c)
            max_len = max(max_len, len(res))
        return max_len
