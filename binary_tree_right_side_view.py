"""
Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.
Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
Time complexity: O(N) since one has to visit each node.
Space complexity: O(D) to keep the queues, where D is a tree diameter. Let's use the last level to estimate the queue
size. This could be up to N/2 tree nodes in the case of complete binary tree.
"""
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        Time complexity: O(N) to visit each node.
        Space complexity: O(D) to keep the queues, where D is a tree diameter. Let's use the last level to estimate
        the queue size. This level could contain up to N/2 tree nodes in the case of complete binary tree.
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                if i == level_len - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
