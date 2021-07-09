"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        stack = []
        for brace in s:
            last_brace = ""
            if brace == "(" or brace == "{" or brace == "[":
                stack.append(brace)
                continue
            if stack:
                last_brace = stack.pop()
            if brace == ")" and last_brace != "(":
                return False
            elif brace == "}" and last_brace != "{":
                return False
            elif brace == ']' and last_brace != "[":
                return False

        return len(stack) == 0
