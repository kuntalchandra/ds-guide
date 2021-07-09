"""
Number of Visible Nodes from Left

There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes
at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a
level could be a right node.
Signature
int visibleNodes(Node root) {
Input
The root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between
0 and 1,000,000,000
Output
An int representing the number of visible nodes.
Example
            8  <------ root
           / \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13
output = 4
"""
from collections import deque


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Add any helper functions you may need here


def visible_nodes(root):
    if not root:
        return 0
    q = deque()
    q.append(root)
    res = []
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == 0:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return len(res)
