"""
Maximum Average Subtree

Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of
the actual answer will be accepted.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.



Example 1:


Input: root = [5,6,1]
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
Example 2:

Input: root = [0,null,1]
Output: 1.00000

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def __init__(self):
        self.max_avg = float("-inf")

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if not root:
            return None
        self.dfs(root)
        return self.max_avg

    def dfs(self, node: TreeNode) -> (float, int):
        if not node:
            return 0, 0
        sum_left, left_count = self.dfs(node.left)
        sum_right, right_count = self.dfs(node.right)
        total_sum = (sum_left + sum_right) + node.val
        total_nodes = (left_count + right_count) + 1
        temp_avg = (total_sum / total_nodes)
        if temp_avg > self.max_avg:
            self.max_avg = temp_avg
        return total_sum, total_nodes
