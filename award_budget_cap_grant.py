"""
Award budget cap

The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget
allocation problem they’re facing. Originally, the committee planned to give N research grants this year. However, due
to spending cutbacks, the budget was reduced to new_budget dollars and now they need to reallocate the grants. The
committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on
all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal
to cap, obviously, won’t be impacted.
Given an array grants_array of the original grants and the reduced budget new_budget, write a function findGrantsCap
that finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new
budget constraint is met (i.e. sum of the N reallocated grants equals to new_budget).

Use Greedy approach
Time complexity: O(NLogN)
Space complexity: O(1)
"""
from typing import List
from unittest import TestCase


def find_grants_cap(grants_array: List[float], new_budget: float) -> float:
    grants_array.sort()
    sum_ = 0
    length = len(grants_array)
    for i in range(length):
        curr = grants_array[i]
        remaining_grants = length - i
        remaining_budget = new_budget - sum_
        if curr * remaining_grants > remaining_budget:
            return remaining_budget / remaining_grants
        sum_ += curr


class TestFindGrantsCap(TestCase):
    def setUp(self) -> None:
        self.grants_1 = [2, 100, 50, 120, 1000]
        self.budget_1 = 190
        self.grants_2 = [2, 4]
        self.budget_2 = 3
        self.grants_3 = [2, 4, 6]
        self.budget_3 = 3
        self.grants_4 = [2, 100, 50, 120, 167]
        self.budget_4 = 400
        self.grants_5 = [21, 100, 50, 120, 130, 110]
        self.budget_5 = 140
        self.grants_6 = [210, 200, 150, 193, 130, 110, 209, 342, 117]
        self.budget_6 = 1530

    def test_find_grants_cap(self) -> None:
        self.assertEqual(47, find_grants_cap(self.grants_1, self.budget_1))
        self.assertEqual(1.5, find_grants_cap(self.grants_2, self.budget_2))
        self.assertEqual(1, find_grants_cap(self.grants_3, self.budget_3))
        self.assertEqual(128, find_grants_cap(self.grants_4, self.budget_4))
        self.assertEqual(23.8, find_grants_cap(self.grants_5, self.budget_5))
        self.assertEqual(211, find_grants_cap(self.grants_6, self.budget_6))
