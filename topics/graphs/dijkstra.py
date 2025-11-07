from typing import List
from collections import defaultdict
from math import inf
from heapq import heappop, heappush

edges = [[0,1,5],[0,3,12],[0,2,7],[1,4,7],[1,2,9],[2,3,4],[2,4,4],[2,5,3],[3,5,7],[4,5,2],[4,6,5],[5,6,2]]
adj = defaultdict(list)
n = 0
for u,v,w in edges:
    adj[u].append((w, v))
    adj[v].append((w, u))
    n = max(u,v,n)

parent = defaultdict(lambda: -1)

def dijkstra(start: int):
    distance = defaultdict(lambda: inf)
    q = []
    u = start
    distance[start] = 0
    tree = set()
    min_weight = 0

    while u not in tree:
        tree.add(u)
        if u != start:
            min_weight += dist

        for weight, v in adj[u]:
            if weight + distance[u] < distance[v]:
                distance[v] = weight + distance[u]
                parent[v] = u
                heappush(q, (weight + distance[u], v))

        while u in tree and q:
            dist, u = heappop(q)

    return min_weight

print(dijkstra(0))
