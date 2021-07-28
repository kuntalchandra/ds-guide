"""
Given a graph and two nodes X and Y, determine if a path exists between X and Y
The following represents a directed graph using adjacency list representation. Use BFS to check path between s and d
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_reachable(self, s, d):
        visited = [False] * self.vertices
        queue = list()
        queue.append(s)
        visited[s] = True
        while queue:
            n = queue.pop(0)
            if n == d:
                return True
            for i in self.graph[n]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return False


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    u = 1
    v = 3
    if g.is_reachable(u, v):
        print("There is a path from {} to {}".format(u, v))
    else:
        print("There is no path from {} to {}".format(u, v))

    u = 3
    v = 1
    if g.is_reachable(u, v):
        print("There is a path from {} to {}".format(u, v))
    else:
        print("There is no path from {} to {}".format(u, v))