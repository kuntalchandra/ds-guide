"""
takes root node and return if its a valid bst

    10
5
  12
"""
from unittest import TestCase


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    """
    Additional space
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        arr = list()
        arr = self.in_order(root, arr)
        if len(set(arr)) != len(arr):
            return False
        copied_arr = arr[:]
        copied_arr.sort()
        return copied_arr == arr

    def in_order(self, node: TreeNode, arr: list) -> list:
        if not node:
            return
        self.in_order(node.left, arr)
        arr.append(node.val)
        self.in_order(node.right, arr)
        return arr


def is_valid_bst(root: TreeNode) -> bool:
    return bst_helper(root, float("-inf"), float("inf"))


def bst_helper(node: TreeNode, min_: float, max_: float):
    if not node:
        return True
    if node.val < min_ or node.val > max_:
        return False
    return bst_helper(node.left, min_, node.val - 1) and bst_helper(node.right, node.val + 1, max_)


class BSTTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_is_valid_bst_false(self):
        obj = TreeNode(10)
        obj.left = TreeNode(5)
        obj.left.right = TreeNode(12)
        self.assertFalse(is_valid_bst(obj))

    def test_is_valid_bst_false_extended_children(self):
        obj = TreeNode(10)
        obj.left = TreeNode(5)
        obj.left.left = TreeNode(8)
        obj.left.right = TreeNode(12)
        self.assertFalse(is_valid_bst(obj))

    def test_is_valid_bst_true(self):
        obj = TreeNode(10)
        obj.left = TreeNode(5)
        self.assertTrue(is_valid_bst(obj))

    def test_is_valid_bst_single_node(self):
        obj = TreeNode(10)
        self.assertTrue(is_valid_bst(obj))

    def test_is_valid_bst_invalid_node(self):
        self.assertTrue(is_valid_bst(None))
