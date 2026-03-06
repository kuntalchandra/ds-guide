"""
Problem:
Design a hit counter that counts hits in the past 5 minutes (300 seconds).
void hit(timestamp) — record a hit at timestamp (seconds granularity, calls in order).
int getHits(timestamp) — return hits in [timestamp - 299, timestamp].

Example:
hit(1), hit(2), hit(3), getHits(4) → 3
hit(300), getHits(300) → 4
getHits(301) → 3  (hit at t=1 is now outside the 300s window)

Approach:
Circular buffer of size 300. Each slot stores (timestamp, count).
On hit: if slot's timestamp == current_timestamp, increment count.
If stale (different timestamp), overwrite with (current_timestamp, 1).
On getHits: sum counts from all 300 slots where timestamp > current_timestamp - 300.

Time: hit O(1), getHits O(300) = O(1)
Space: O(300) = O(1)

Triggers:
- sliding window count over fixed time range
- circular buffer for time-series data
- "rate limiter with history"

Variants / Watch-outs:
- Optimisation angle: deque-based solution is O(n) where n = hits in window;
  circular buffer is O(1) regardless — the key is bounding by time range not hit count
- Logger Rate Limiter is the simpler cousin — recognise the family
- Follow-up: what if timestamps are not in order? Need sorted structure (deque + cleanup)
"""

class Solution:
    def __init__(self):
        self.times = [0] * 300
        self.counts = [0] * 300

    def hit(self, timestamp):
        idx = timestamp % 300
        if self.times[idx] == timestamp:
            self.counts[idx] += 1
        else:
            self.times[idx] = timestamp     # overwrite stale slot
            self.counts[idx] = 1

    def get_hits(self, timestamp):
        total = 0
        for idx in range(300):
            if self.times[idx] > timestamp - 300:
                total += self.counts[idx]
        return total