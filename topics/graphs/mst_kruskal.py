from typing import List
from union_find import UnionFind, union, same
# from heapq import heappush, heappop

edges = [[0,1,5],[0,3,12],[0,2,7],[1,4,7],[1,2,9],[2,3,4],[2,4,4],[2,5,3],[3,5,7],[4,5,2],[4,6,5],[5,6,2]]
n = 0
for u,v,_ in edges: n = max(n,u,v)

def kruskal(edges: List[List[int]], n: int):
    q = sorted(edges, key=lambda x: x[2])
    s, weight = UnionFind(n + 1), 0

    for u,v,w in q:
        if not same(s, u, v):
            weight += w
            union(s, u, v)

    return weight

print(kruskal(edges, n))
