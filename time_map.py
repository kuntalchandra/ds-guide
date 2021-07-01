"""
Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with
timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest
timestamp_prev. If there are no values, it returns "".
"""

from bisect import bisect_right
from collections import defaultdict
from unittest import TestCase


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.meta = defaultdict(list)
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]


class TestTimeMap(TestCase):
    def setUp(self):
        pass

    def test_time_map(self):
        time_map = TimeMap()
        time_map.set("love", "high", 10)
        time_map.set("love", "low", 20)
        self.assertEqual("high", time_map.get("love", 10))
        self.assertEqual("high", time_map.get("love", 15))
        self.assertEqual("low", time_map.get("love", 20))
        self.assertEqual("low", time_map.get("love", 25))

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
