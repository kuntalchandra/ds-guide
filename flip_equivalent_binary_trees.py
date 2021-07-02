"""
Flip Equivalent Binary Trees
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.


Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Example 4:
Input: root1 = [0,null,1], root2 = []
Output: false

Example 5:
Input: root1 = [0,null,1], root2 = [0,1]
Output: true


     1
   /   \
  2     3
 / \   /
4   5 6
   /\
  7  8
     1
   /   \
  3     2
   \   / \
    6 4   5
         /\
        8  7
Approach:
* DFS both roots simultaneously
* If one of them is None, both should be None.
* If root1's left node value is not equal to root2's left node value, flip root1's children
* If root1's left node is None and root2's left node is not, flip root1's children
* If root2's left node is None and root1's left node is not, flip root1's children
Time complexity: O(n1 + n2)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 == root2
        if ((root1.left and root2.left and root1.left.val != root2.left.val) or (not root1.left and root2.left) or (
                root1.left and not root2.left)):
            root1.left, root1.right = root1.right, root1.left
        return (root1.val == root2.val and self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right,
                                                                                                     root2.right))
