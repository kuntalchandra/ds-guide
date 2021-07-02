"""
Calculate the amount of tax needs to be paid.

Given a tax bracket which consists of the tax slab and tax percentage, calculate the amount of tax you need to pay.
Assume, the tax bracket is sorted by applicable interest rates.

Example 1:
Input: tax brackets: [[2500, 0.0], [5000, 0.05], [10000, 0.2], [None, 0.3]], income: 55000
Output: 7000
Explanation: No tax till 2500. So, next slab computes tax of 125. Till next slab the total tax is 1125. Overall, tax to
be paid is 12375

Example 2:

Input: tax brackets: [[5000, 0.0], [None, 0.1]], income: 500
Output: 0

Example 3:

Input: tax brackets: [[None, 0.3]], income: 10000
Output: 3000
"""
from typing import List, Any
from unittest import TestCase


def calculate_tax(slabs: List[List[Any]], salary: int) -> float:
    if not slabs:
        return 0
    min_slab = slabs[0][0]
    if min_slab and salary < min_slab:
        return 0
    tax = 0
    remaining_salary = salary
    prev_slab = 0

    for slab in slabs:
        amount, percent = slab
        if not amount:
            break
        applicable_amount = amount - prev_slab
        remaining_salary -= amount
        tax += (applicable_amount * percent)
        prev_slab = amount

    if not amount and percent:
        tax += (remaining_salary * percent)
    return tax


class TestCalculateTax(TestCase):
    def setUp(self) -> None:
        self.slabs_1 = [[2500, 0.0], [5000, 0.05], [10000, 0.2], [None, 0.3]]
        self.income_1 = 55000
        self.slabs_2 = [[5000, 0.0], [None, 0.1]]
        self.income_2 = 500
        self.slabs_3 = [[None, 0.3]]
        self.income_3 = 10000

    def test_calculate_tax(self) -> None:
        self.assertEqual(12375, calculate_tax(self.slabs_1, self.income_1))
        self.assertEqual(0, calculate_tax(self.slabs_2, self.income_2))
        self.assertEqual(3000, calculate_tax(self.slabs_3, self.income_3))
