"""
Find a node which is reachable from all other nodes

https://leetcode.com/playground/8AzHyy6o
https://leetcode.com/discuss/interview-question/1238472/Find-a-node-which-is-reachable-from-all-other-nodes-or-Phone
https://leetcode.com/discuss/interview-question/867806/q3-online-microsoft-interview-finding-rome

Find a node which is reachable from all other nodes

Given two arrays A & B where A[i] is connected to B[i], find a node which is reachable from all other nodes. If there
are no such nodes, then return -1

Examples:
A = [0,1,2,4,5], B = [2,3,3,3,2]
Output - 3
Explanation - 0->2, 1->3, 2->3, 4->3, 5->2, here only node 3 is reachable from all the other nodes

A = [2,3,3,4], B = [1,1,0,0]
Output : -1
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B):
    # write your code in Python 3.6
    return reachable_nodes(A, B)


def convert_to_adjacency_list(A, B):
    adj_list = [[] for _ in range(len(A) + 1)]
    for i, node in enumerate(A):
        neighbor = B[i]
        adj_list[node].append(neighbor)
    return adj_list


def reachable_nodes(A, B):
    if len(A) != len(B) or not A or not B:
        return -1

    adj_list = convert_to_adjacency_list(A, B)
    nodes_no_degrees = []

    for node, neighbors in enumerate(adj_list):
        if len(neighbors) == 0:
            nodes_no_degrees.append(node)

    return nodes_no_degrees[0] if len(nodes_no_degrees) == 1 else -1
