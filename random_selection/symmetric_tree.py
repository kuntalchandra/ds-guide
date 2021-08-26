"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false

"""
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, node_1: TreeNode, node_2: TreeNode) -> bool:
        if not node_1 and not node_2:
            return True
        if not node_1 or not node_2:
            return False
        return (node_1.val == node_2.val) and self.is_mirror(node_1.left, node_2.right) and self.is_mirror(node_1.right,
                                                                                                           node_2.left)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root.left, root.right])
        while q:
            node_1, node_2 = q.popleft(), q.popleft()
            if not node_1 and not node_2:
                continue
            elif not node_1 or not node_2:
                return False
            elif node_1.val != node_2.val:
                return False
            q.extend([node_1.left, node_2.right, node_1.right, node_2.left])
        return True
