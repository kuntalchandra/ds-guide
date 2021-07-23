"""
Binary Tree Pruning


Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1
has been removed.

A subtree of a node node is node plus every node that is a descendant of node.



Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # Return the pruned tree if it contains a 1 else null
        return root if self.contains_one(root) else None

    def contains_one(self, node: TreeNode) -> bool:
        if not node:
            return False

        # Check if any node in the left subtree contains a 1
        left_contains_one = self.contains_one(node.left)
        # Check if any node in the right subtree contains a 1
        right_contains_one = self.contains_one(node.right)

        # If not, prune the left subtree
        if not left_contains_one:
            node.left = None
        # If not, prune the right subtree
        if not right_contains_one:
            node.right = None

        # Return true if the current node or its left or right subtree contains a 1
        return node.val or left_contains_one or right_contains_one
