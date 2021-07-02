"""
Find Leaves of Binary Tree

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
"""
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        while root:
            curr_leaves = []
            root = self.find_leaves(root, curr_leaves)
            res.append(curr_leaves)
        return res

    def find_leaves(self, root: TreeNode, curr_leaves: List) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            curr_leaves.append(root.val)
            return None
        if root.left:
            root.left = self.find_leaves(root.left, curr_leaves)
        if root.right:
            root.right = self.find_leaves(root.right, curr_leaves)
        return root
