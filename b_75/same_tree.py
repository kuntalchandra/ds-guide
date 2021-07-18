"""
Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tree_1 = self.pre_order(p, [])
        tree_2 = self.pre_order(q, [])
        return tree_1 == tree_2

    def pre_order(self, node: TreeNode, arr: List[int]) -> List[int]:
        if not node:
            arr.append(-1)
            return arr
        arr.append(node.val)
        self.pre_order(node.left, arr)
        self.pre_order(node.right, arr)
        return arr
