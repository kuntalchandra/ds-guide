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

Similar variation-
Bracket Match
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a
later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For
instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and
returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2

"""
from unittest import TestCase


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


def bracket_match(text):
    """
    Time/ Space: O(n)
    """
    if not text:
        return 0
    stack = []    # ""
    for bracket in text:  # "(())"
        if stack:
            last_bracket = stack.pop()  # "("
            if last_bracket == "(":
                if bracket == "(":
                    stack.extend([last_bracket, bracket])
            else: # ")"
                stack.extend([last_bracket, bracket])
        else:
            stack.append(bracket)   # "("
    return len(stack)

"""
Time/ Space: O(n) and O(1)
function bracketMatch(text):
    diffCounter = 0
    ans = 0
    n = text.length

    for i from 0 to n-1:
        if ( text[i] == '(' ):
            diffCounter += 1
        else if ( text[i] == ')' ):
            diffCounter -= 1
        if ( diffCounter < 0 ):
            diffCounter += 1
            ans += 1

    return ans + diffCounter
"""


class TestValidParenthesis(TestCase):
    def setUp(self) -> None:
        self.s_1 = ""
        self.s_2 = "()"
        self.s_3 = "()[]{}"
        self.s_4 = "(]"
        self.s_5 = "([)]"
        self.s_6 = "{[]}"
        self.s_7 = "[])"

    def test_valid_parenthesis(self) -> None:
        obj = Solution()
        self.assertTrue(obj.isValid(self.s_1))
        self.assertTrue(obj.isValid(self.s_2))
        self.assertTrue(obj.isValid(self.s_3))
        self.assertFalse(obj.isValid(self.s_4))
        self.assertFalse(obj.isValid(self.s_5))
        self.assertTrue(obj.isValid(self.s_6))
        self.assertFalse(obj.isValid(self.s_7))

    def test_bracket_match(self):
        self.assertEqual(1, bracket_match("(()"))
        self.assertEqual(0, bracket_match("(())"))
        self.assertEqual(2, bracket_match("())("))
