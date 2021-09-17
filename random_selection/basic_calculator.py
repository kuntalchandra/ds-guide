"""
Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of
the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as
eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

"""
from typing import Any, List


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0
        for ch in range(len(s) - 1, -1, -1):
            if s[ch].isdigit():
                # form the operand in reverse order.
                operand = (10 ** n * int(s[ch])) + operand
                n += 1
            elif s[ch] != " ":
                if n:
                    # save the operand as it's a non digit
                    stack.append(operand)
                    n, operand = 0, 0
                if s[ch] == "(":
                    res = self.evaluate_stack(stack)
                    stack.pop()
                    # store the result as it could be a sub-result of inner parenthesis
                    stack.append(res)
                else:
                    # other characters can be pushed to stack directly
                    stack.append(s[ch])
        # push if anything left over
        if n:
            stack.append(operand)
        return self.evaluate_stack(stack)

    def evaluate_stack(self, stack: List[Any]) -> int:
        res = stack.pop() if stack else 0
        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == "+":
                res += stack.pop()
            else:
                res -= stack.pop()
        return res