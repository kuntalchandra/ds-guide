"""
Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


Approach:
BFS level-order with alternating collection direction.
Use a deque per level — appendleft when going right-to-left, append normally otherwise.
Flip direction flag after every level.

from collections import deque
queue = deque([root])
result = []
left_to_right = True

while queue:
    level_size = len(queue)
    level = deque()
    for _ in range(level_size):
        node = queue.popleft()
        if left_to_right: level.append(node.val)
        else: level.appendleft(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(list(level))
    left_to_right = not left_to_right

Triggers:
- zigzag / spiral level order traversal
- alternating direction per level
- same BFS skeleton, only the collection changes

Variants / Watch-outs:
- Don't reverse the BFS queue — only flip how you BUILD each level's result list
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        res = []
        q = deque()
        q.append(root)

        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)

        for i, values in enumerate(res):
            if i % 2 == 1:
                res[i] = reversed(values)

        return res
