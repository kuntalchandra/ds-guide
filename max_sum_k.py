"""
Given an array of integers of size n. Find the maximum sum of k
Time complexity: O(n)
"""
from unittest import TestCase


def sum_k(array: list, k: int) -> int:
    if k > len(array):
        return False
    m = sum(array[:k])
    for i in range(len(array)):
        if (i + k) <= len(array):
            m = max(m, sum(array[i: i + k]))
    return m


def sum_k_window_slicing(array: list, k: int):
    if k > len(array):
        return False
    m = sum(array[:k])
    window_sum = m
    for i in range(len(array) - k):
        window_sum = window_sum - array[i] + array[i + k]
        m = max(window_sum, m)
    return m


class TestSumK(TestCase):
    def setUp(self) -> None:
        self.input_array_1 = [100, 200, 300, 400]
        self.input_k_1 = 2
        self.input_array_2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
        self.input_k_2 = 4
        self.input_array_3 = [2, 3]
        self.input_k_3 = 3

    def test_sum_k(self):
        self.assertEqual(700, sum_k(self.input_array_1, self.input_k_1))
        self.assertEqual(39, sum_k(self.input_array_2, self.input_k_2))
        self.assertFalse(sum_k(self.input_array_3, self.input_k_3))

    def test_sum_k_window_slicing(self):
        self.assertEqual(700, sum_k_window_slicing(self.input_array_1, self.input_k_1))
        self.assertEqual(39, sum_k_window_slicing(self.input_array_2, self.input_k_2))
        self.assertFalse(sum_k_window_slicing(self.input_array_3, self.input_k_3))
