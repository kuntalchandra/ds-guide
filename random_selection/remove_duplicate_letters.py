"""
Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your
result is the smallest in lexicographical order among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        stack = []
        order = {c: i for i, c in enumerate(s)}

        for idx, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and idx < order[stack[-1]]:
                    last_char = stack.pop()
                    seen.discard(last_char)
                stack.append(char)
                seen.add(char)
        return "".join(stack)
