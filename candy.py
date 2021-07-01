from typing import List
from unittest import TestCase

"""
Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
TIme complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        return sum(candies)


class TestCandy(TestCase):
    def setUp(self):
        self.ratings_1 = [1, 0, 2]
        self.ratings_2 = [1, 2, 2]

    def test_candy(self):
        obj = Solution()
        self.assertEqual(5, obj.candy(self.ratings_1))
        self.assertEqual(4, obj.candy(self.ratings_2))
