"""
Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even
indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Approach 1:
Find the odd, even elements and build the new list. This is leading to additional space.

Follow up: You must solve the problem in O(1) extra space complexity and O(n) time complexity
Approach- Put the odd nodes in a linked list and the even nodes in another. Then link the evenList to the tail of the
oddList.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        odd, even = [], []
        sentinel = dummy = ListNode(0)
        i = 0
        while head:
            if i % 2 == 0:
                odd.append(head.val)
            else:
                even.append(head.val)
            head = head.next
            i += 1
        for i in range(len(odd)):
            sentinel.next = ListNode(odd[i])
            sentinel = sentinel.next
        for i in range(len(even)):
            sentinel.next = ListNode(even[i])
            sentinel = sentinel.next
        return dummy.next

    def oddEvenListOptimised(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        i = 1
        while head:
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            i += 1
        odd.next = dummy2.next
        even.next = None
        return dummy1.next
