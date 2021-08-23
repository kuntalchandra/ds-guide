"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            current = nums[i]
            diff = target - current
            if current in maps:
                return [maps[current], i]
            maps[diff] = i
        return


"""
Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such 
that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true

"""


class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = self.inorder(root, [])
        left, right = 0, len(arr) - 1
        while left < right:
            total = arr[left] + arr[right]
            if total == k:
                return True
            if total < k:
                left += 1
            else:
                right -= 1
        return False

    def inorder(self, node: TreeNode, arr: List[int]) -> List[int]:
        if node:
            self.inorder(node.left, arr)
            arr.append(node.val)
            self.inorder(node.right, arr)
        return arr
