from typing import List
from collections import defaultdict
from algos.graphs.utils import visualize_undirected

edges = [[0,18],[18,1],[1,19],[21,20],[20,7],[7,8],[3,22],[22,13],[13,1],[13,9],[9,16],[16,7],[24,17],[17,3],[3,21],[22,6],[6,11],[11,7],[23,4],[4,15],[15,12],[5,7],[7,21],[21,1]]
visualize_undirected(edges)
n = max((v for edge in edges for v in edge))
adj = defaultdict(list)
weight = {}

for x,y in edges:
    adj[x].append(y)
    adj[y].append(x)

discovered = set()
def dfs(v: int, component: List):
    discovered.add(v)
    component.append(v)
    for u in adj[v]:
        if u not in discovered:
            dfs(u, component)
    return component

components: List[List[int]] = []
for v in range(n):
    if v not in discovered:
        components.append(dfs(v, []))

components.sort(key= lambda x: len(x), reverse=True)
current = n + 1
for component in components:
    component.sort(key=lambda x: len(adj[x]), reverse=True)
    for v in component:
        weight[v] = current
        current -= 1

parents = defaultdict(lambda: -1)
discovered, processed = set(), set()
def dfsw(v: int):
    discovered.add(v)
    current = 0
    for u in adj[v]:
        if u not in discovered:
            current += (weight[v] + weight[u])
            parents[u] = v
            current += dfsw(u)
        elif u not in processed and parents[v] != u:
            current += (weight[v] + weight[u])
    processed.add(v)
    return current

total = 0
for v in range(n):
    if v not in discovered:
        total += dfsw(v)

print(total)
