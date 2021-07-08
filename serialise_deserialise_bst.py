"""
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or
memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another
computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to
a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
Time complexity: O(n)
Space complexity: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        arr = self.pre_order(root, [])
        return " ".join([str(x) for x in arr])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        arr = data.split(" ")
        root = TreeNode(int(arr.pop(0)))
        for val in arr:
            self.create_tree(root, int(val))
        return root

    def pre_order(self, root: TreeNode, arr: []) -> List[str]:
        if root:
            arr.append(root.val)
            self.pre_order(root.left, arr)
            self.pre_order(root.right, arr)
        return arr

    def create_tree(self, root, val: int) -> TreeNode:
        while True:
            if val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
