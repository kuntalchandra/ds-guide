"""
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Approach:
Push head of each list into a min-heap as (value, list_idx, node).
Repeatedly extract minimum, attach to result, push that node's next.
Heap always holds at most k elements.

dummy = ListNode(0)
current = dummy
heap = []

for idx, node in enumerate(lists):
    if node:
        heappush(heap, (node.val, idx, node))

while heap:
    value, idx, node = heappop(heap)
    current.next = node
    current = current.next
    if node.next:
        heappush(heap, (node.next.val, idx, node.next))

return dummy.next

Time: O(N log k) where N = total nodes, k = number of lists
Space: O(k) for heap

Triggers:
- merge k sorted sources
- streaming merge from multiple feeds
- "combine k sorted results from distributed systems"

Variants / Watch-outs:
- Optimisation angle: naive merge-two-at-a-time is O(Nk); heap is O(N log k);
  divide-and-conquer pairwise is also O(N log k) — same complexity but no extra space
- Use list index as tiebreaker in heap tuple to avoid comparing ListNodes
"""


from typing import List
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        """
        O(nLogn)
        """
        res = []
        dummy = head = ListNode(-1)

        for l in lists:
            while l:
                res.append(l.val)
                l = l.next
        for value in sorted(res):
            dummy.next = ListNode(value)
            dummy = dummy.next
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        O(Nlogk)
        """
        dummy = head = ListNode(-1)
        q = PriorityQueue()

        for l in lists:
            if l:
                q.put((l.val, l))

        while q:
            value, node = q.get()
            dummy.next = ListNode(value)
            dummy = dummy.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
