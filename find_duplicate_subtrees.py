"""
Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

            1
           / \
         2    3
        /    / \
       4    2   4
           /
          4

Input: root = [2,1,1]
Output: [[1]]

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Note: tree_str = self.post_order(root.left) + self.post_order(root.right) + str(root.val)
Input:
[10,2,22,1,12,1,1]
Output:
[[1],[22,1,1]]
Expected:
[[1]]
"""
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tree_str_count = defaultdict(int)
        self.res = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.post_order(root)
        return self.res

    def post_order(self, root: TreeNode):
        if not root:
            return "#"

        tree_str = self.post_order(root.left) + "#" + self.post_order(root.right) + "#" + str(root.val)
        if self.tree_str_count[tree_str] == 1:
            self.res.append(root)
        self.tree_str_count[tree_str] += 1
        return tree_str
