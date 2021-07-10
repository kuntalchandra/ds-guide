"""
Given a set of array, find one which doesn't belong to others
"""
from typing import List
from unittest import TestCase


def find_anomaly(values: List[List[str]]) -> List[str]:
    max_common = list()
    for curr_list in values:
        max_ = 0
        other_lists = [i for i in values if i != curr_list]
        for next_list in other_lists:
            curr_common = len(set(next_list).intersection(curr_list))
            if curr_common > max_:
                max_ = curr_common
        max_common.append(max_)
    return values[max_common.index(min(max_common))]


class TestFindAnomaly(TestCase):
    def setUp(self) -> None:
        self.sets_1 = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'e'], ['g', 'h', 'i', 'j']]
        self.sets_2 = [['g', 'h', 'i', 'j'], ['a', 'b', 'c', 'd'], ['a', 'b', 'e', 'j']]
        self.sets_3 = [['a', 'b', 'c', 'd'], ['g', 'h', 'i', 'j'], ['g', 'h', 'a', 'b']]

    def test_find_anomaly(self):
        self.assertListEqual(['g', 'h', 'i', 'j'], find_anomaly(self.sets_1))
        self.assertListEqual(['g', 'h', 'i', 'j'], find_anomaly(self.sets_2))
        self.assertListEqual(['a', 'b', 'c', 'd'], find_anomaly(self.sets_3))