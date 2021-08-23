"""
Minimum Absolute Difference in BST
Minimum Distance Between BST Nodes

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two
different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1

Time Complexity: O(N), where N is the number of nodes in the tree. We iterate over every node once.
Space Complexity: O(H), where H is the height of the tree. This is the space used by the implicit call stack when
calling dfs in recursive dfs implementation. Otherwise, O(N) additional space used to store all the node values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = self.inorder(root, [])
        """
        Use 2 variables to calculate the min while iterating the nodes will optimise this additional pass
        self.ans = min(self.ans, node.val - self.prev)
        self.prev = node.val
        """
        return min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))

    def inorder(self, node: TreeNode, arr: List[int]) -> List[int]:
        if node:
            self.inorder(node.left, arr)
            arr.append(node.val)
            self.inorder(node.right, arr)
        return arr
