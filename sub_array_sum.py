"""
Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals to k


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Approach-
Calculate cumulative sum and store in hashmap. If there is a increase of k, then that's a subarray.
Consider the difference between 0 to k in the c_sum by addressing {0: 1}
Time complexity: O(n)
Spce complexity: O(n)


Mental model:
Prefix sum + hashmap. At each index, prefix_sum = sum(nums[0..idx]).
We want to count how many times (prefix_sum - k) has appeared before —
that means a subarray ending here sums to k.
Seed the map with {0: 1} to handle subarrays starting from index 0.

prefix_count = {0: 1}
current_sum = 0
count = 0

for num in nums:
    current_sum += num
    diff = current_sum - k
    if diff in prefix_count:
        count += prefix_count[diff]
    prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

return count

Time: O(n)
Space: O(n) for prefix_count map

Triggers:
- count subarrays summing to exactly k
- any "how many contiguous subarrays satisfy X" problem
- negative numbers present (sliding window won't work — use prefix sum)

Variants / Watch-outs:
- Optimisation angle: sliding window only works for non-negative arrays; prefix sum +
  hashmap is the general O(n) solution that handles negatives
- Subarray Sum Divisible by K: store prefix_sum % k as key instead
- Maximum Size Subarray Sum = k: store first-seen index of each prefix_sum instead of count
"""
from typing import List
from unittest import TestCase


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c_sum = {0: 1}
        counter, curr_sum = 0, 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in c_sum:
                counter += c_sum[diff]

            if curr_sum in c_sum:
                c_sum[curr_sum] += 1
            else:
                c_sum[curr_sum] = 1
        return counter


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.nums_1 = [1, 1, 1]
        self.k_1 = 2
        self.nums_2 = [1, 2, 3]
        self.k_2 = 3
        self.nums_3 = [1, 2, 1, 2, 1]
        self.k_3 = 3

    def testSubarraySum(self) -> None:
        obj = Solution()
        self.assertEqual(2, obj.subarraySum(self.nums_1, self.k_1))
        self.assertEqual(2, obj.subarraySum(self.nums_2, self.k_2))
        self.assertEqual(4, obj.subarraySum(self.nums_3, self.k_3))
