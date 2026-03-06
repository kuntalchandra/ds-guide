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



Approach:
Count frequencies with Counter. Use a min-heap of size k — push (frequency, element).
When heap exceeds k, pop the minimum. At the end, heap contains the k most frequent.

count = Counter(nums)
heap = []

for element, frequency in count.items():
    heappush(heap, (frequency, element))
    if len(heap) > k:
        heappop(heap)           # evict least frequent

return [element for frequency, element in heap]

Time: O(n log k) — n elements, each heap op is log k
Space: O(n) for count map + O(k) for heap

Triggers:
- top k by some frequency/score
- min-heap of size k for "top k maximum" problems
- O(n log k) beats O(n log n) sort when k << n

Variants / Watch-outs:
- Optimisation angle: sort is O(n log n); heap is O(n log k) — for small k this is a big win
- Bucket sort approach: O(n) — frequency is bounded by n, use array of size n+1 as buckets
- Top K Frequent Words: same pattern, but need lexicographic tiebreak —
  heap element becomes (frequency, word), negate frequency for max-heap behaviour
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
