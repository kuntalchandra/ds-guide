"""
Different Ways to Add Parentheses

Given a string expression of numbers and operators, return all possible results from computing all the different
possible ways to group numbers and operators. You may return the answer in any order.



Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Worth to check: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-concise-solution-with-memorization
https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/866096/Python%3A-Divde-and-Conquer-%2B-Memoization-%2B-O(N-*-2N)

Time Complexity: O(N * 2^N)
Let N be the length of the expression
In the worst case there are N // 2 operations: when all expression numbers are numbers of 1 digits
For example, expression: 1+2+3+4+5+6
len(expression) = 11
operations # = 5
Therefore, our recursion depth is O(N/2)
		depth         Nbr of problem           work at corresponding depth
		0             1                        O(N) #divide expression
		1             2                        O(1) + O(N - 2) = O(N) * 2
		...
		i             2^i                      O(N) * 2^i
		...
		N//2          2^N//2                   O(N) * 2^N//2

		Total time complexity: O(N) (2^0 + 2^1 + ... + 2^N//2) = O(N * 2^N//2) = O(N * 2^N)

"""
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.dp(expression, {})

    def dp(self, expression: str, memo: dict) -> List[int]:
        if expression in memo:
            return memo[expression]
        if expression.isdigit():
            memo[expression] = int(expression)
            return [int(expression)]
        res = []
        for idx, char in enumerate(expression):
            if char in "+-*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])

                for l in left:
                    for r in right:
                        res.append(self.helper(l, r, char))
        memo[expression] = res
        return res

    def helper(self, input_1: int, input_2: 2, operator: str) -> int:
        if operator == "+":
            return input_1 + input_2
        elif operator == "-":
            return input_1 - input_2
        else:
            return input_1 * input_2
