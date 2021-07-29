"""
Absolute Value Sort

TODO: Follow up
Given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values
of the numbers in arr. If two numbers have the same absolute value, sort them according to sign, where the negative
numbers come before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]
"""
from unittest import TestCase


def absSort(arr):
    for i in range(len(arr)-2):
        best = i
        for j in range(i, len(arr)-1):
            if smaller(arr[j], arr[best]):
                best = j
            arr[best], arr[i] = arr[i], arr[best]
    return arr


def smaller(a: int, b: int):
    if abs(a) < abs(b):
        return True
    if abs(a) > abs(b):
        return False
    return a < b


class TestSort(TestCase):
    def setUp(self) -> None:
        self.input = [2, -7, -2, -2, 0]

    def test_sort(self):
        self.assertListEqual([0, -2, -2, 2, -7], absSort(self.input))
