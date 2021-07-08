"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""
from heapq import heappush, heapify, heappop
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(nlogn)
        Space complexity: O(k)
        """
        if not nums:
            return []
        count = Counter(nums)  # O(n)
        count = sorted(count.items(), key=lambda n: n[1], reverse=True)  # O(nLogn)
        res = []
        for key, value in count:
            res.append(key)
            if len(res) == k:
                break
        return res

    def topKFrequentMostCommon(self, nums: List[int], k: int) -> List[int]:
        return [element[0] for element in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(Nlog(k))
        Space complexity: O(k)
        """
        if not nums:
            return []
        count = Counter(nums)  # O(n)
        heap = []

        for key, value in count.items():  # O(k)
            heappush(heap, (value, key))  # O(logn)

            if len(heap) > k:
                heappop(heap)  # O(logn)

        res = []
        while heap:  # O(k)
            frequency, key = heappop(heap)
            res.append(key)

        return res
