"""
Delete Nodes And Return Forest
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

      1
  2       3
4   5   6   7
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        del_set = set(to_delete)
        q = deque([(root, False)])

        while q:
            node, has_parent = q.popleft()

            # Found new root
            if not has_parent and node.val not in del_set:
                res.append(node)

            has_parent = not node.val in del_set

            if node.left:
                q.append((node.left, has_parent))
                if node.left.val in del_set:
                    node.left = None
            if node.right:
                q.append((node.right, has_parent))
                if node.right.val in del_set:
                    node.right = None
        return res
