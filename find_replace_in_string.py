"""
Find And Replace in String

You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are
given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

Example 2:
Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.
"""
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        modified = list(s)
        for index, source, target in zip(indices, sources, targets):
            if not s[index:].startswith(source):
                continue
            else:
                for i in range(index, len(source) + index):
                    modified[i] = ""
                modified[index] = target

        return "".join(modified)
