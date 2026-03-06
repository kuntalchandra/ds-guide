"""
Problem:
Design a data structure that supports:
addNum(num) — add a number to the stream
findMedian() — return the median of all numbers so far

Example:
addNum(1), addNum(2), findMedian() → 1.5
addNum(3), findMedian() → 2.0

Approach:
Two heaps: max-heap for lower half (invert sign in Python), min-heap for upper half.
Invariant: lower half size == upper half size OR lower half has one extra.
On add: always push to lower first, then balance by pushing lower's max to upper.
If upper becomes bigger, push upper's min back to lower.
Median: if equal sizes → average of both tops; if lower is bigger → lower's max.

import heapq
self.lower = []     # max-heap (negate values)
self.upper = []     # min-heap

def add_num(num):
    heappush(self.lower, -num)              # push to lower
    heappush(self.upper, -heappop(self.lower))   # balance: move lower's max to upper
    if len(self.upper) > len(self.lower):   # keep lower >= upper in size
        heappush(self.lower, -heappop(self.upper))

def find_median():
    if len(self.lower) > len(self.upper):
        return -self.lower[0]
    return (-self.lower[0] + self.upper[0]) / 2.0

Time: addNum O(log n), findMedian O(1)
Space: O(n)

Triggers:
- median of a growing stream
- split data into two halves with O(log n) rebalancing
- "two heaps" pattern for order statistics

Variants / Watch-outs:
- Optimisation angle: naive sort-on-every-add is O(n log n) per call;
  two heaps gives O(log n) add and O(1) median
- Sliding Window Median (LC 480): heaps + lazy deletion — significantly harder
- The double-push (push to lower, immediately move max to upper) is the clean
  way to maintain the invariant without separate if/else
"""