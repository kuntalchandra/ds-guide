"""
Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
It is guaranteed that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before
the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the
intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do
not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Follow up: Space complexity : O(1)
Approach: 2 pointers with 2 dummy nodes
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Space complexity : O(N).
        As we are storing each of the nodes from list1 into a hash table, the hash table will require O(N) space.
        Note that we could have instead stored the nodes of list2, this would have been a space complexity of O(N).
        Unless we know which list is longer though, it doesn't make any real difference.
        Time complexity : O(N + M)
        Firstly, build up the hash table or set. It costs O(1) to insert an item, and need to do this for each of the
        M nodes in iterating list . This gives a cost of O(M) for building. Secondly, we need to traverse next list A,
        and for each node, need to check whether or not it is in the set. In the worst case, there will not be a match,
        requiring to check all N nodes in list. As it is also O(1) to check whether or not an item is there,
        this checking has a total cost of O(N).
        Finally, combining the two parts, we get O(M) + O(N) = O(M+N).
        """
        dummy_set = set()
        while headA:
            dummy_set.add(headA)
            headA = headA.next
        while headB:
            if headB in dummy_set:
                return headB
            headB = headB.next
        return
