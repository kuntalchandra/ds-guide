"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a
subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.
Given tree s:
     3
    / \
   4   5
  / \
 1   2
 Given tree t:
   4
  / \
 1   2
Output = true
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Output = false
Time complexity : O(m*n) In worst case(skewed tree) traverse function takes O(m*n) time.
Space complexity : O(n) The depth of the recursion tree can go upto n. n refers to the number of nodes in s
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return root and (
                self.is_equal(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,
                                                                                                     subRoot))

    def is_equal(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        else:
            return (root.val == subRoot.val) and self.is_equal(root.left, subRoot.left) and self.is_equal(root.right,
                                                                                                          subRoot.right)
