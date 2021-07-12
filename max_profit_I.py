"""
Best Time to Buy and Sell Stock I
Given an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete
at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit
Note that you cannot sell a stock before you buy one.
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float("+inf")
        if not prices:
            return profit
        for price in prices:
            if price < min_price:
                min_price = price
            elif (price - min_price) > profit:
                profit = (price - min_price)
        return profit


class TestProfit(TestCase):
    def setUp(self) -> None:
        self.prices_1 = [7,1,5,3,6,4]
        self.prices_2 = [7,6,4,3,1]

    def test_profit(self) -> None:
        obj = Solution()
        self.assertEqual(5, obj.maxProfit(self.prices_1))
        self.assertEqual(0, obj.maxProfit(self.prices_2))
