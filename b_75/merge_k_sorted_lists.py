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
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue


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
