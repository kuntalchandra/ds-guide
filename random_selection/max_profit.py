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
        min_price, max_profit = prices[0], float("-inf")
        for idx in range(len(prices)):
            min_price = min(min_price, prices[idx])
            profit = prices[idx] - min_price
            max_profit = max(profit, max_profit)
        return max_profit


class TestProfit(TestCase):
    def setUp(self) -> None:
        self.prices_1 = [7, 1, 5, 3, 6, 4]
        self.prices_2 = [7, 6, 4, 3, 1]

    def test_profit(self) -> None:
        obj = Solution()
        self.assertEqual(5, obj.maxProfit(self.prices_1))
        self.assertEqual(0, obj.maxProfit(self.prices_2))


"""
Best Time to Buy and Sell Stock II
Design an algorithm to find the maximum profit from the prices array where each elements present the price of ith day.
1. Multiple transactions are allowed
2. Buy before sell, sell before buy again
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution1:
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
        obj = Solution1()
        self.assertEqual(7, obj.maxProfit(self.prices_1))
        self.assertEqual(4, obj.maxProfit(self.prices_2))
        self.assertEqual(0, obj.maxProfit(self.prices_3))


"""
Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions with the same rule Buy
before sell, sell before buy again
TIme complexity: O(n)
"""


class Solution2:
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


class TestSolution2(TestCase):
    def setUp(self) -> None:
        self.prices_1 = [3, 3, 5, 0, 0, 3, 1, 4]
        self.prices_2 = [1, 2, 3, 4, 5]
        self.prices_3 = [7, 6, 4, 3, 1]

    def testMaxProfit(self) -> None:
        obj = Solution2()
        self.assertEqual(6, obj.maxProfit(self.prices_1))
        self.assertEqual(4, obj.maxProfit(self.prices_2))
        self.assertEqual(0, obj.maxProfit(self.prices_3))


"""
Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times) with the following restrictions:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Approach:
Respect: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75940/5-lines-Python-O(n)-time-O(1)-space
free is the maximum profit I can have while being free to buy.
have is the maximum profit I can have while having stock.
cool is the maximum profit I can have while cooling down.
"""


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        have = cool = float("-inf")
        for price in prices:
            free, have, cool = max(free, cool), max(have, free - price), have + price
        return max(free, cool)
