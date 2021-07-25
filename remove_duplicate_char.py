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
        # keep the last occurrence which will tell that no more s[i] is left in s
        last_occur = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            # keep only one of each char unless it's not already there
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occur[stack[-1]]:
                    last_c = stack.pop()
                    seen.discard(last_c)
                stack.append(c)
                seen.add(c)

        return "".join(stack)
