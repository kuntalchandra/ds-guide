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
Sliding window with a hashmap storing char → last seen index.
On encountering a duplicate, jump left directly to last_seen + 1
(not a slow shrink). This avoids iterating the shrink step character by character.

seen = {}
left = 0
best = 0

for right, ch in enumerate(s):
    if ch in seen and seen[ch] >= left:     # duplicate within current window
        left = seen[ch] + 1                 # jump directly, not shrink-by-1
    seen[ch] = right
    best = max(best, right - left + 1)

return best

Time: O(n) — each char processed at most twice (once added, once jumped past)
Space: O(min(n, charset)) for seen map

Triggers:
- longest substring with no repeats
- shrink window on first constraint violation
- O(n) with direct-jump optimisation

Variants / Watch-outs:
- Optimisation angle: naive O(n²) scans for the duplicate; hashmap gives O(1) jump
- The seen[ch] >= left check matters — a stale entry from before left is irrelevant
- At Most K Distinct Characters: replace seen with a count map, shrink when map size > k

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
