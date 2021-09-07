"""
Binary Tree Longest Consecutive Sequence

Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child
connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).



Example 1:


Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:


Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]  # default
        lcs = 1
        while stack:
            node, length = stack.pop()
            lcs = max(lcs, length)

            if node.left:
                if node.left.val - node.val == 1:
                    stack.append((node.left, length + 1))
                else:
                    stack.append((node.left, 1))

            if node.right:
                if node.right.val - node.val == 1:
                    stack.append((node.right, length + 1))
                else:
                    stack.append((node.right, 1))
        return lcs
