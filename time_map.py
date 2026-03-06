"""
Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key with the value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with
timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest
timestamp_prev. If there are no values, it returns "".


Approach:
For each key, store timestamps in a sorted list and values in a parallel list.
On get: binary search (bisect_right) to find the rightmost timestamp <= query timestamp.
bisect_right returns the insertion point — subtract 1 to get the floor entry.

self.timestamps = defaultdict(list)   # key → [t1, t2, ...]
self.values = defaultdict(list)       # key → [v1, v2, ...]

def set(key, value, timestamp):
    self.timestamps[key].append(timestamp)   # timestamps arrive in order
    self.values[key].append(value)

def get(key, timestamp):
    idx = bisect_right(self.timestamps[key], timestamp)
    if idx == 0: return ""          # no timestamp <= query
    return self.values[key][idx - 1]

Time: set O(1), get O(log n) where n = entries for that key
Space: O(total set calls)

Triggers:
- retrieve value at or before a given timestamp
- versioned/historical data lookup
- binary search on sorted timestamps

Variants / Watch-outs:
- Optimisation angle: current solution is optimal; naive is linear scan O(n) per get
- Snapshot Array uses same bisect_right pattern — recognise the family
- If timestamps are not guaranteed ascending on set, you'd need to sort — clarify this upfront
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
