"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        """
        Additional space + additional pass
        """
        sentinel = dummy = ListNode(0)
        length = 0
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            length += 1
        if n == 1:
            arr = arr[:-1]
        else:
            arr = arr[:-n] + arr[-n + 1:]

        for num in arr:
            dummy.next = ListNode(num)
            dummy = dummy.next

        return sentinel.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Approch:
        Use two pointers. The first pointer advances the list by n+1 steps from the beginning, while the second pointer
        starts from the beginning of the list. Now, both pointers are exactly separated by n nodes apart. Maintain this
        constant gap by advancing both pointers together until the first pointer arrives past the last node. The second
        pointer will be pointing at the nth node counting from the last. Relink the next pointer of the node referenced
        by the second pointer to point to the node's next next node.
        """
        second = first = head
        i = 0
        while second:
            second = second.next
            i += 1
            if i > n + 1:
                first = first.next

        if i == n:
            return head.next
        first.next = first.next.next
        return head
