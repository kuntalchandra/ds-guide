"""
Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all
nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        This approach doesn't get any benefit from the fact that the tree is a complete one
        """
        arr = self.preorder(root, [])
        return len(arr)

    def preorder(self, node: TreeNode, arr: List[int]) -> List[int]:
        if node:
            arr.append(node.val)
            self.preorder(node.left, arr)
            self.preorder(node.right, arr)
        return arr

    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Tree has 2^d - 1 nodes across all levels except the last one
        Level 0: 2^0 nodes, 1: 2^1 nodes, 2: 2^2 nodes, k: 2^k nodes, last level d: 1 <= nodes <= 2^d
        total nodes = 2^d - 1 + last level nodes

        Time complexity : O(d^2)=O(log^2 * N), where d is a tree depth.
        Space complexity : O(1).
        """
        if not root:
            return 0
        # get the tree depth
        depth = self.compute_depth(root)
        # only root is there
        if depth == 0:
            return 1
        # last level nodes are enumerated from 0 to 2 ** depth - 1 using left to right order
        # binary search to find out how many nodes exist
        left, right = 0, 2 ** depth - 1
        while left <= right:
            mid = (left + right) // 2
            if self.exists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1

        # 2 ** depth - 1 nodes on the depth - 1 level and left nodes on the last level
        return (2 ** depth - 1) + left

    def compute_depth(self, node: TreeNode) -> int:
        """
        O(depth) time complexity to determine the depth
        """
        depth = 0
        while node.left:
            node = node.left
            depth += 1
        return depth

    def exists(self, mid: int, depth: int, node: TreeNode) -> bool:
        left, right = 0, 2 ** depth - 1
        # last level nodes are enumerated from 0 to 2**depth - 1 using left to right order
        # binary search with O(depth) time complexity to find if last level node idx exists
        for _ in range(depth):
            pivot = (left + right) // 2
            if mid <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
