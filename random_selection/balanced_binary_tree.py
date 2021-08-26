"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # subtrees must be having height <= 1 and subtrees must be following the same balancing rule
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def height(self, node: TreeNode) -> int:
        # empty tree has height -1
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
