"""
Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary
search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by
more than one.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.create_tree(0, len(nums) - 1, nums)

    def create_tree(self, left: int, right: int, nums: List[int]) -> TreeNode:
        if left > right:
            return
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.create_tree(left, mid - 1, nums)
        root.right = self.create_tree(mid + 1, right, nums)
        return root
