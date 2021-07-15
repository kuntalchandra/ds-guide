"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item. Both the operations must be done in
O(1) time complexity
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
