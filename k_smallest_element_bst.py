"""
Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.



Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth
smallest frequently, how would you optimize?

Credit: https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
The time complexity of insert and delete operations is O(H), where H is a height of binary tree, and H = logN for the
balanced tree. Hence without any optimisation insert/delete + search of kth element has O(2H+k) complexity.

How to optimise that?

Actually this implies to implement a structure which contains a BST inside and optimises the following operations :
Insert
Delete
Find kth smallest

Seems like a database description, isn't it? Let's use here the same logic as for LRU cache design, and combine an
indexing structure (we could keep BST here) with a double linked list.

Such a structure would provide:
O(H) time for the insert and delete.
O(k) for the search of kth smallest.

The overall time complexity for insert/delete + search of kth smallest is O(H+k) instead of O(2H+k).

Complexity Analysis
Time complexity for insert/delete + search of kth smallest: O(H+k), where H is a tree height. O(logN+k) in the
average case, O(N+k) in the worst case.
Space complexity : O(N) to keep the linked list.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Time complexity : O(N) to build a traversal.
        Space complexity : O(N) to keep an inorder traversal
        """
        arr = self.helper(root, [])
        return arr[k - 1]

    def helper(self, node: TreeNode, arr: List[int]) -> List[int]:
        if node:
            self.helper(node.left, arr)
            arr.append(node.val)
            self.helper(node.right, arr)
        return arr
