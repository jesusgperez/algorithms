from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent: List[int] = [i for i in range(n)]
        self.size: list[int] = [1 for i in range(n)]


def find(s: UnionFind, u: int):
    if s.parent[u] == u:
        return u

    return find(s, s.parent[u])


def union(s: UnionFind, u: int, w: int):
    root_u, root_w = find(s, u), find(s, w)

    if root_u == root_w:
        return

    if s.size[root_u] >= s.size[root_w]:
        s.size[root_u] += s.size[root_w] 
        s.parent[root_w] = root_u
    else:
        s.size[root_w] += s.size[root_u]
        s.parent[root_u] = root_w


def same(s: UnionFind, u: int, w: int):
    return find(s, u) == find(s, w)
