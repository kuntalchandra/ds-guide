"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item. Both the operations must be done in
O(1) time complexity



Approach:
OrderedDict gives O(1) get/put/move-to-front in Python — it maintains
insertion order and exposes move_to_end().
On get: move accessed key to front (most recent).
On put: if at capacity, popitem() removes from the BACK (least recent).
Always move to front after any access.

self.cache = OrderedDict()
self.capacity = capacity

def get(key):
    if key not in self.cache: return -1
    self.cache.move_to_end(key, last=False)   # move to front = most recent
    return self.cache[key]

def put(key, value):
    if key in self.cache:
        self.cache[key] = value
    else:
        if len(self.cache) == self.capacity:
            self.cache.popitem()              # remove from back = least recent
        self.cache[key] = value
    self.cache.move_to_end(key, last=False)   # always move to front

Time: O(1) for both get and put
Space: O(capacity)

Triggers:
- O(1) get + O(1) evict-least-recently-used
- cache with bounded size
- "design a system that keeps the most recently used items"

Variants / Watch-outs:
- Optimisation angle: naive dict + list is O(n) for eviction; OrderedDict is O(1);
  raw doubly-linked-list + hashmap is the explicit O(1) implementation interviewers love
- LFU Cache: harder — need frequency buckets + OrderedDict per bucket
- move_to_end(key, last=False) = front; last=True (default) = back — easy to mix up
"""
from collections import OrderedDict
from unittest import TestCase


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = -1
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
            value = self.cache[key]
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem()
            self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        return


class TestLRUCache(TestCase):
    def setUp(self) -> None:
        pass

    def testCacheCycle(self) -> None:
        cache = LRUCache(2)
        self.assertIsNone(cache.put(2, 1))
        self.assertIsNone(cache.put(2, 2))
        self.assertEqual(2, cache.get(2))
        self.assertIsNone(cache.put(1, 1))
        self.assertIsNone(cache.put(4, 1))
        self.assertEqual(-1, cache.get(2))

    def testCacheCycle1(self) -> None:
        cache = LRUCache(2)
        self.assertIsNone(cache.put(1, 1))
        self.assertIsNone(cache.put(2, 2))
        self.assertEqual(1, cache.get(1))
        self.assertIsNone(cache.put(3, 3))
        self.assertEqual(-1, cache.get(2))
        self.assertIsNone(cache.put(4, 4))
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(3, cache.get(3))
        self.assertEqual(4, cache.get(4))

    def testCacheCycle2(self) -> None:
        cache = LRUCache(2)
        self.assertIsNone(cache.put(2, 1))
        self.assertIsNone(cache.put(1, 1))
        self.assertIsNone(cache.put(2, 3))
        self.assertIsNone(cache.put(4, 1))
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(3, cache.get(2))
