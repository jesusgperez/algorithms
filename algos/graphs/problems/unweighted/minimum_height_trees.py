from typing import List
from collections import deque


def create_undirected(n: int, edges: List[List[int]]):
    adj = [[] for _ in range(n)]
    degree = [0 for _ in range(n)]

    for x ,y in edges:
        adj[x].append(y)
        adj[y].append(x)
        degree[x] += 1
        degree[y] += 1

    return adj, degree


adj, degree = create_undirected(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])

queue = deque(v for v, deg in enumerate(degree) if deg == 1)

center = []

while queue:
    center.clear()
    for _ in range(len(queue)):
        leaf = queue.popleft()
        center.append(leaf)

        for v in adj[leaf]:
            degree[v] -= 1
            if degree[v] == 1:
                queue.append(v)

# The center is the response
# Those vertices in the center of a tree are the ones with the minimum height
# No need to find all the heights of every vertice
