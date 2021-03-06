"""
Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The
binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

      1
    /  \
   2    3
 / \   /  \
4  5  6   7

       1       --> NULL
    /    \
   2 ---> 3    --> NULL
 / \     / \
4-->5-> 6-->7  --> NULL

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree, your function should populate each next pointer to point to its next
right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#'
signifying the end of each level.
"""
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        q = deque([root])

        while q:
            length = len(q)

            for i in range(length):
                node = q.popleft()
                if i < length - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
