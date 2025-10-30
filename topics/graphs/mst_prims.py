from pydantic import BaseModel
from typing import List, Tuple
from math import inf
from collections import defaultdict


class Edge(BaseModel):
    val: int
    weight: int
    next: 'Edge'


class Graph(BaseModel):
    edges: List[Edge]
    degree: List[int]
    n_edges: int
    n_vertices: int


g = Graph()


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


def prim(start: int, adj: List[Tuple[int, int]]):
    distance = defaultdict(lambda: inf)
    parent = defaultdict(lambda: -1)
    tree = set()

    distance[start] = 0
    v = start
    weight = 0

    while v not in tree:
        tree.add(v)

        if v != start:
            print(parent[v], '->', v)
            weight += dist

        for w, weight in adj[v]:
            if weight < distance[w] and w not in tree:
                distance[w] = weight
                parent[w] = v

        dist = inf
        for w in range(len(adj)):
            if distance[w] < dist and not w in tree:
                dist = distance[w]
                v = w

    return weight



