"""
Pairs with specific difference

Variation- 2 Sum
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that
returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.
Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]
input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []

Time Complexity: O(N)
Space Complexity: O(N)
"""
from unittest import TestCase


def find_pairs_with_given_difference(arr, k):
    if not arr or not k:
        return []

    hashmap = dict()
    pairs = list()

    for x in arr:
        hashmap[x - k] = x

    for y in arr:
        if y in hashmap:
            pairs.append([hashmap[y], y])
    return pairs


class TestPairsWithGivenDifference(TestCase):
    def setUp(self) -> None:
        self.arr_1 = [4, 1]
        self.k_1 = 3
        self.arr_2 = [1, 5, 11, 7]
        self.k_2 = 4

    def test_find_pairs_with_given_difference(self) -> None:
        self.assertListEqual([[4, 1]], find_pairs_with_given_difference(self.arr_1, self.k_1))
        self.assertListEqual([[5, 1], [11, 7]], find_pairs_with_given_difference(self.arr_2, self.k_2))