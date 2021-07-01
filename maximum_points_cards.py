"""
Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points. The points are given in
the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints:
            return 0
        points = sum(cardPoints[:k])
        max_points = points
        n = len(cardPoints) - 1

        for i in range(1, k + 1):
            points += cardPoints[-i] - cardPoints[k - i]
            max_points = max(max_points, points)

        return max_points


class TestMaxScore(TestCase):
    def setUp(self):
        self.card_points_1 = [1, 2, 3, 4, 5, 6, 1]
        self.card_points_2 = [1, 79, 80, 1, 1, 1, 200, 1]
        self.k = 3

    def test_max_score(self) -> None:
        obj = Solution()
        self.assertEqual(12, obj.maxScore(self.card_points_1, self.k))
        self.assertEqual(202, obj.maxScore(self.card_points_2, self.k))
