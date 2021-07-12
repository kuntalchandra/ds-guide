"""
Coin Change I
Variation: Monsoon Umbrella

You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2

Approach:
F(3) = min{F(3−c1),F(3−c2),F(3−c3)}+1
=min{F(3−1),F(3−2),F(3−3)}+1
=min{F(2),F(1),F(0)}+1
=min{1,1,0}+1
=1

coins   1       2       3           F(i)
Amount                              min() + 1
1       F(0)    -       -           1
2       F(1)    F(0)    -           1
3       F(2)    F(1)    F(0)        1
4       F(3)    F(2)    F(1)        2
5       F(4)    F(3)    F(2)        2
6       F(5)    F(4)    F(3)        2

Time complexity : O(S∗n). On each step the algorithm finds the next F(i) in n iterations, where 1 ≤ i ≤ S. Therefore
in total the iterations are S∗n.
Space complexity : O(S). We use extra space for the memoization table
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if not amount:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


"""
Coi Change II
You are given coins of different denominations and a total amount of money. Write a function to compute the number of
combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Approach: DP
table[row][col] = table[row - 1][col] + table[row][col - coins[row - 1]]
            0   1   2   3   4   5
[]          1   0   0   0   0   0
[1]         1   1   1   1   1   1
[1, 2]      1   1   2   2   3   3
[1, 2, 5]   1   1   2   2   3   4
"""
from typing import List


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1  # 0 amount = 1 way
        for coin in coins:
            for i in range(coin, amount + 1):
                # if i >= coin:
                ways[i] = ways[i] + ways[i - coin]
        # print(ways)
        return ways[amount]
