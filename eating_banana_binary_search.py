"""
Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and
will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas
from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Approach:
With piles = [3, 6, 7, 11] and H = 8, there is some X = 4 so that possible(1) = possible(2) = possible(3) = False, and
possible(4) = possible(5) = ... = True
Binary search in [1, max(piles)] to find the k.
Binary search on the values of possible(K) to find the first X such that possible(X) is True, that will be the answer.
Time complexity: O(NlogM)
"""
from math import ceil

from typing import List


class Solution(object):
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p-1) / K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) / 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo


class Solution1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if sum(ceil(pile / mid) for pile in piles) > h:
                low = mid + 1
            else:
                high = mid
        return low
̨