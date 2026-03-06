"""
Snapshot Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
Credit: https://leetcode.com/problems/snapshot-array/discuss/350562/JavaPython-Binary-Search


Approach:
Don't store a full copy of the array per snapshot — that's O(n) per snap.
Instead, per index store only the (snap_id, value) pairs for changes made to that index.
On get(index, snap_id): binary search for the latest change at or before snap_id.

self.snap_id = 0
self.snaps = [[ [-1, 0] ] for _ in range(length)]   # each index starts with sentinel

def set(index, val):
    self.snaps[index].append([self.snap_id, val])

def snap():
    self.snap_id += 1
    return self.snap_id - 1

def get(index, snap_id):
    idx = bisect_right(self.snaps[index], [snap_id + 1]) - 1
    return self.snaps[index][idx][1]

Time: set O(1), snap O(1), get O(log s) where s = snaps on that index
Space: O(total set calls) — vastly better than O(n × snaps)

Triggers:
- point-in-time / versioned array lookups
- sparse updates across many snapshots
- "what was the value at time T"

Variants / Watch-outs:
- Optimisation angle: naive O(n) copy per snap fails at scale — the key insight is
  only changed indices need recording (sparse update pattern)
- Sentinel [-1, 0] handles "no changes before snap_id 0" — needed to avoid idx going -1
- Same bisect_right trick as Time Map — the [snap_id + 1] is to find insertion point
  AFTER snap_id, then -1 gives the floor
"""
from bisect import bisect_right
from unittest import TestCase


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snaps = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snaps[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_right(self.snaps[index], [snap_id + 1]) - 1
        return self.snaps[index][idx][1]


class TestSnapshotArray(TestCase):
    def setUp(self) -> None:
        pass

    def test_snapshot_array(self):
        snapshot = SnapshotArray(3)
        self.assertIsNone(snapshot.set(0, 5))
        self.assertEqual(0, snapshot.snap())
        self.assertIsNone(snapshot.set(0, 6))
        self.assertEqual(5, snapshot.get(0, 0))
