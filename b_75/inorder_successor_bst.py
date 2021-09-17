"""
Inorder Successor in BST

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If
the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        successor = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor


"""
Inorder Successor in BST II

Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no 
in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent 
node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
Example 2:


Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Example 3:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17
Example 4:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15
Example 5:

Input: tree = [0], node = 0
Output: null

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        """
        Successor: It's the after node i.e. the next node or the smallest node after the current one in inorder traversal
        Predecessor: It's the before node i.e. the previous node or the largest node before the current one.

        Algo-
        1. If the node has a right child, its successor is somewhere lower in the tree.
        Go to the right once and then as left as possible. Return the last possible node
        2. If no right child, then must be somewhere in the upper tree. Go up till the node
        that is left child of its parent. Return that node's parent

        Time: O(H), where H is the height of the tree i.e. O(logN) in the average case.
        O(N) in the worst case, where N is the number of nodes in the tree.
        Space: O(1)
        """
        # successor belongs to somewhere in the right i.e. lower subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # successor belongs to somewhere in the upper tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
