"""
Max Number of Distinct Notes along a Root-Node Path
https://leetcode.com/discuss/interview-question/1065005/Max-Number-of-Distinct-Notes-along-a-Root-Node-Path/850343

            1  <------ root
           / \
         2     3
        / \   / \
       3   6 3   1
      /         /\
    2          5  6
"""


def max_distinct_node(root: TreeNode) -> int:
    return helper(root, set())


def helper(root: TreeNode, seen_set: set) -> int:
    if not root or root.val in seen_set:
        return len(seen_set)
    seen_set.add(root.val)
    left = helper(root.left, seen_set)
    right = helper(root.right, seen_set)
    seen_set.remove(root.val)
    return max(left, right)
