"""
Shuffle an Array

Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should
be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.


Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

Time complexity : O(n)

The Fisher-Yates algorithm runs in linear time, as generating a random index and swapping two values can be done in
constant time.

Space complexity : O(n)

Although we managed to avoid using linear space on the auxiliary array from the brute force approach, we still need
it for reset, so we're stuck with linear space complexity.
"""
from random import randrange
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.original
        self.original = list(self.original)
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        length = len(self.arr)
        for i in range(length):
            idx = randrange(i, length)
            self.arr[i], self.arr[idx] = self.arr[idx], self.arr[i]
        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
