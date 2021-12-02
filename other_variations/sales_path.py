"""
Sales Path

Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root
is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node
and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In
addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

                0
            /   |    \
           5    3     6
        /      / \   /\
       4      2   0 1  5
            /    /
           1    10
          /
        1

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a
Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree
above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function
getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost
is 7: 0→6→1 and 0→3→2→1→1)
"""


def get_cheapest_cost(rootNode):
    """
    Time Complexity: let N be the number of nodes in the tree. Notice that getCheapestCost is applied to every node
    exactly once. Therefore, there are overall O(N) calls to getCheapestCost.

    Space Complexity: every time the function recurses, it consumes only a constant amount of space. However, due to
    the nature of the recursion we used, the stack call holds N instances of getCheapestCost which makes the total
    space complexity to be O(N).
    """
    children = rootNode.children()

    if not children:
        return rootNode.cost
    else:
        min_cost = float("inf")
        for child in children:
            temp_cost = get_cheapest_cost(child)
            min_cost = min(min_cost, temp_cost)
    return min_cost + rootNode.cost


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None
