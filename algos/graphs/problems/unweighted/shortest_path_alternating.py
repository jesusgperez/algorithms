from typing import Dict, List
from collections import defaultdict

red = [[0,1],[1,2],[2,3],[3,4]]
blue = [[0,1],[1,2],[3,3]]
red = [[0,1],[1,2],[2,3],[3,4]]
blue = [[1,2],[2,3],[3,1]]
red = [[0,1],[1,2]]
blue = [[1,0]]

adj = defaultdict(lambda: defaultdict(list))

def create_graph(blue: List[List[int]], red: List[List[int]]):
    for x, y in blue:
        adj[x]['blue'].append(y)

    for x, y in red:
        adj[x]['red'].append(y)

create_graph(blue, red)

def pick_color(color: str):
    if color == 'red':
        return 'blue'
    return 'red'

paths = [-1 if i != 0 else i for i in range(5)]

def dfs(v: int, color: str, length: int):

    for u in adj[v][color]:
        if (v,u) not in discovered[color]:
            discovered[color].add((v,u))
            paths[u] = length if paths[u] == -1  else min(paths[u], length)
            dfs(u, pick_color(color), length + 1)

discovered = defaultdict(set)
dfs(0, 'blue', 1)

discovered = defaultdict(set)
dfs(0, 'red', 1)

print(paths)
