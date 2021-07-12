"""
Best Time to Buy and Sell Stock II
Design an algorithm to find the maximum profit from the prices array where each elements present the price of ith day.
1. Multiple transactions are allowed
2. Buy before sell, sell before buy again
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                max_profit += (prices[i] - prices[i - 1])
        return max_profit


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.prices_1 = [7, 1, 5, 3, 6, 4]
        self.prices_2 = [1, 2, 3, 4, 5]
        self.prices_3 = [7, 6, 4, 3, 1]

    def testMaxProfit(self):
        obj = Solution()
        self.assertEqual(7, obj.maxProfit(self.prices_1))
        self.assertEqual(4, obj.maxProfit(self.prices_2))
        self.assertEqual(0, obj.maxProfit(self.prices_3))
