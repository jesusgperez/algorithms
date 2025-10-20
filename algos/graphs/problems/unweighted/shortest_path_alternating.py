from typing import Dict, List
from collections import defaultdict

red = [[0,1],[1,2],[2,3],[3,4]]
blue = [[0,1],[1,2],[3,3]]
red = [[0,1],[1,2],[2,3],[3,4]]
blue = [[1,2],[2,3],[3,1]]

adj_red = defaultdict(list)
adj_blue = defaultdict(list)

def create_graph(adj: Dict, edges: List[List[int]]):
    for x, y in edges:
        adj[x].append(y)

create_graph(adj_red, red)
create_graph(adj_blue, blue)

def pick_adj(adj: List[List[int]]):
    if adj == adj_red:
        return adj_blue
    return adj_red

def pick_discovered(disc):
    if disc == blue_discovered:
        return red_discovered
    return blue_discovered

paths = [-1 if i != 0 else i for i in range(5)]

def dfs(v: int, adj: List[List[int]], disc: set, length: int):
    disc.add(v)

    for u in adj[v]:
        if u not in disc:
            paths[u] = length if paths[u] == -1  else min(paths[u], length)
            dfs(u, pick_adj(adj), pick_discovered(disc), length + 1)

blue_discovered = set()
red_discovered = set()
dfs(0, adj_blue, red_discovered, 1)
blue_discovered = set()
red_discovered = set()
dfs(0, adj_red, blue_discovered, 1)

print(paths)
