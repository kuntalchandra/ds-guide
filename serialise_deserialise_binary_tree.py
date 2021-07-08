"""
Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to
a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
need to follow this format, so please be creative and come up with different approaches yourself.


Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example:
You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]"
Approach: BFS pre-order traversal

Time complexity: O(n)
Space complexity: O(n)
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        q = deque([root])
        arr = []

        while q:
            node = q.popleft()
            if not node:
                arr.append("None")
                continue
            arr.append(str(node.val))
            q.extend([node.left, node.right])
        return " ".join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = deque(data.split(" "))
        root = TreeNode(int(nodes.popleft()))
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                left, right = nodes.popleft(), nodes.popleft()

                if left == "None":
                    node.left = None
                else:
                    node.left = TreeNode(int(left))

                if right == "None":
                    node.right = None
                else:
                    node.right = TreeNode(int(right))
                q.extend([node.left, node.right])
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
