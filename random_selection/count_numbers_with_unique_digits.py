"""
Count Numbers with Unique Digits

Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.



Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1

"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        res = 10  # possible result
        choices = 9  # number of choices for the leading digit i.e. 1, 2, 3 ... 9
        for i in range(1, n):
            # remaining choices for the ith digit after fixing the digits preceding it and last digit
            # e.g. for i = 2, fixing the first and last digit leaves 8 choices for the second digit
            choices = choices * (10 - i)
            res += choices
        return res
