"""
Weird Faculty

https://leetcode.com/discuss/interview-question/374440/Twitter-or-OA-2019-or-Weird-Faculty
Given n questions and predetermined marks list, find the minimum k such that your result > your friend's result. Marks
are predetermined e.g. the marks array is given marks = [1, 0, 0, 1, 0] and the verdict of ith question is marks[i].

Answer first k questions (indices 0 to k-1) and your friend has to answer the remaining questions (indices k to n-1). 0
is considered to deduct marks.

Input: [1, 0, 0, 1, 0]
Output: 0
If you answer 0 questions i.e. k = 0, your result = 0 and friend's result = -2 because of 2 correct and 3 wrong answers.

Input: [1, 0, 0, 1, 1]
Output: 1

Input: [1, 1, 1, 0, 1]
Output: 2
"""
from typing import List
from unittest import TestCase


def weird_faculty(marks: List[int]) -> int:
    if not marks:
        return 0
    # modify the marks to update 0 to -1
    for i, mark in enumerate(marks):
        if mark == 0:
            marks[i] = -1

    total_sum = sum(marks)
    current_sum = 0

    # find out the position where current sum is greater than total sum
    for i, mark in enumerate(marks):
        if current_sum > total_sum:
            return i
        current_sum += mark
        total_sum -= mark

    return len(marks)


class TestWeirdFaculty(TestCase):
    def setUp(self) -> None:
        self.marks_1 = [1, 0, 0, 1, 0]
        self.marks_2 = [1, 0, 0, 1, 1]
        self.marks_3 = [1, 1, 1, 0, 1]

    def test_weird_sum(self) -> None:
        self.assertEqual(0, weird_faculty(self.marks_1))
        self.assertEqual(1, weird_faculty(self.marks_2))
        self.assertEqual(2, weird_faculty(self.marks_3))
