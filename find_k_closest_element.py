"""
Find k closest element

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result
should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
Time complexity: O(log(N)+k).
Space complexity: O(1)
"""
from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # base case
        if len(arr) == k:
            return arr

        # find the closest element and initialise 2 pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # till the window size is less than k
        while right - left - 1 < k:
            # check boundary
            if left == -1:
                right += 1
                continue

            # expand the window towards the closest number with the considertion of the boundary
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        # this is the window
        return arr[left + 1: right]
