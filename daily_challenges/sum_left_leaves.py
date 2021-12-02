"""
Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0

Input: root = [1,2,3,4,5]
Output: 4

Input: root = [9,null,2,0,null,-7,null,-1]
Output = -1
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Time/ Space: O(N)
        It's not told whether or not the input tree is balanced (most non-leaf nodes having 2 children, thus minimizing
        the maximum depth). Therefore, need to assume it is not. However, if asked what the time and space complexity
        are if the input was guaranteed to be a balanced tree. If it is, balanced, then the time complexity remains the
        same (still have to visit all N nodes), but the space complexity becomes O(D), where D is the maximum depth.
        This is equivalent to O(logN).
        """
        if not root:
            return 0
        q = deque()
        q.append(root)
        res = 0
        while q:
            node = q.popleft()
            if self.is_leaf(node.left):
                res += node.left.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    def is_leaf(self, node: TreeNode) -> bool:
        return node is not None and node.left is None and node.right is None