"""
Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""
from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time complexity: O(nLogn)
        """
        nums.sort(reverse=True)
        return nums[k-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time complexity: O(k + (n-k) log k)
        space complexity: O(k)
        """
        heap = nums[:k]
        heapify(heap)  # O(k)

        for num in nums[k:]:  # O(n-k)
            if num > heap[0]:
                heappop(heap)
                heappush(heap, num)  # O(logk)

        return heap[0]
