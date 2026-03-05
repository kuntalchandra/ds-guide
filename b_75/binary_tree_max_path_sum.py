"""
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through
the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42


Approach:
Define gain(node) = best single arm you can offer your parent.
At each node, evaluate the full arch through it (left_gain + node.val + right_gain)
and update global max. Return only the best single arm upward —
a path through the parent can only use one branch. Clip negatives to 0.

self.max_sum = float('-inf')

def gain(node):
    if not node: return 0
    left_gain  = max(0, gain(node.left))     # clip negative arms
    right_gain = max(0, gain(node.right))
    self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)
    return node.val + max(left_gain, right_gain)  # single arm to parent

Triggers:
- max sum path that can start and end anywhere in the tree
- path can "bend" at one node but cannot branch
- global answer tracked outside recursion, local return serves the parent

Variants / Watch-outs:
- Diameter of Binary Tree: same pattern, count edges (length) instead of sum
- The return value and the global update are intentionally DIFFERENT — that's the core trick
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.calculate(root)
        return self.max_sum

    def calculate(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.calculate(node.left)
        right = self.calculate(node.right)
        self.max_sum = max(self.max_sum, node.val + left + right)
        return max(node.val + max(left, right), 0)
