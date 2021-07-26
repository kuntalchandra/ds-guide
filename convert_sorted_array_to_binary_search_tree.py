"""
Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
binary search tree.

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
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(0, len(nums) - 1, nums)

    def helper(self, left: int, right: int, nums: List[int]) -> TreeNode:
        if left > right:
            return
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid + 1, right, nums)
        return root

    """
    # input: [0,1,2,3,4,5]
    # output: [2,0,3,null,1,null,4,null,null,null,5]
    # expected: [3,1,5,0,2,4]
    # The height is not balanced in this implementation

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left, right = 0, len(nums)- 1
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        nums = nums[:mid] + nums[mid+1:]
        for num in nums:
            self.helper(root, num)
        return root

    def helper(self, root: TreeNode, num: int) -> TreeNode:
        while True:
            if num > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(num)
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(num)
                    break
        return root
    """
