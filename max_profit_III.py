"""
Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions with the same rule Buy
before sell, sell before buy again
TIme complexity: O(n)
"""
from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction
        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.prices_1 = [3, 3, 5, 0, 0, 3, 1, 4]
        self.prices_2 = [1, 2, 3, 4, 5]
        self.prices_3 = [7, 6, 4, 3, 1]

    def testMaxProfit(self) -> None:
        obj = Solution()
        self.assertEqual(6, obj.maxProfit(self.prices_1))
        self.assertEqual(4, obj.maxProfit(self.prices_2))
        self.assertEqual(0, obj.maxProfit(self.prices_3))
