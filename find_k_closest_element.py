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

Approach:
Binary search for the LEFT BOUNDARY of the k-element answer window.
For any left index mid, the window is arr[mid : mid + k].
Compare x - arr[mid] vs arr[mid + k] - x.
Whichever side is farther from x, slide the window away from it.

low, high = 0, len(arr) - k
while low < high:
    mid = (low + high) // 2
    if x - arr[mid] > arr[mid + k] - x:
        low = mid + 1       # left side is farther, slide right
    else:
        high = mid          # right side is farther, slide left
return arr[low : low + k]

Triggers:
- k closest values to a target in a sorted array
- fixed-size sliding window over sorted input
- binary search on window position, not on a value

Variants / Watch-outs:
- x may not exist in the array — that's fine, the comparison still holds
- Use strict > (not >=) to prefer the left side on ties, per problem spec
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

            # expand the window towards the closest number with the consideration of the boundary
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        # this is the window
        return arr[left + 1: right]
