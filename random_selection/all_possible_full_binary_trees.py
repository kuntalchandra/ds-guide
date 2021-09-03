"""
All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer
must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.



Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def __init__(self):
        self.memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.memo:
            res = []
            for x in range(n):
                y = n - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        res.append(node)
            self.memo[n] = res
        return self.memo[n]
