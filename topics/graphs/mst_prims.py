from pydantic import BaseModel
from typing import List, Tuple
from math import inf
from collections import defaultdict
from heapq import heappush, heappop


class Edge(BaseModel):
    val: int
    weight: int
    next: 'Edge'    


class Graph(BaseModel):
    edges: List[Edge]
    degree: List[int]
    n_edges: int
    n_vertices: int


# g = Graph()


def prims(g: Graph, start: int):
    parent = [-1 for _ in range(g.n_vertices)]
    distance = [inf for _ in range(g.n_vertices)]
    in_tree = [False for _ in range(g.n_vertices)]

    distance[start] = 0
    v = start
    dist = 0

    while not in_tree[v]:
        in_tree[v] = True
        if v != start:
            print(parent[v], v)
            weight += dist

        p = g.edges[v]
        while not p:
            w = p.val
            if p.weight < distance[w] and not in_tree[w]:
                distance[w] = p.weight
                parent[w] = v
            p = p.next

        dist = inf
        for w in range(g.n_vertices):
            if not in_tree[w] and distance[w] < dist:
                v = w
                dist = distance[w]

    return weight


def prim(start: int, adj: List[Tuple[int, int]], n: int):
    distance = defaultdict(lambda: inf)
    parent = defaultdict(lambda: -1)
    tree = set()

    distance[start] = 0
    v = start
    min_weight = 0

    while v not in tree:
        tree.add(v)

        if v != start:
            print(parent[v], '->', v)
            min_weight += dist

        for w, weight in adj[v]:
            if weight < distance[w] and w not in tree:
                distance[w] = weight
                parent[w] = v

        dist = inf
        for w in range(n + 1):
            if distance[w] < dist and not w in tree:
                dist = distance[w]
                v = w

    return min_weight


edges = [[0,1,5],[0,3,12],[0,2,7],[1,4,7],[1,2,9],[2,3,4],[2,4,4],[2,5,3],[3,5,7],[4,5,2],[4,6,5],[5,6,2]]
adj = defaultdict(list)

n = 0
for u,v,w in edges:
    adj[u].append((v,w))
    adj[v].append((u,w))
    n = max(n,u,v)

print(prim(0, adj, n))


def prim_heap(start: int, adj: List[Tuple[int, int]], n):
    parent = defaultdict(lambda: -1)
    distance = defaultdict(lambda: inf)
    tree = set()

    v = start
    distance[start] = 0
    min_weight = 0
    q = []

    while not v in tree:
        tree.add(v)
        if v != start:
            print(parent[v], '->', v)
            min_weight += dist

        for w, weight in adj[v]:
            if weight < distance[w] and w not in tree:
                heappush(q, (weight, w))
                distance[w] = weight
                parent[w] = v

        while v in tree and q:
            dist, v = heappop(q)

    return min_weight

print(prim_heap(0, adj, n))
