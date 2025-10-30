from typing import List
from collections import defaultdict
from networkx import draw_networkx, DiGraph
from matplotlib.pyplot import show

red = [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
blue = [[1,3],[0,0],[0,3],[4,2],[1,0]]
red = [[8,6],[2,0],[8,3],[5,1],[1,3],[5,7],[6,8],[6,2]]
blue  = [[0,1],[0,6],[1,4],[2,8],[8,8],[3,3],[3,6],[3,7],[2,1],[4,0],[8,1],[2,2],[1,7],[0,8],[6,5],[7,8],[5,0],[6,7],[5,4]]

n = max(n for edge in red + blue for n in edge) + 1

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

paths = [-1 if i != 0 else i for i in range(n)]

def dfs(v: int, color: str, length: int):
    for u in adj[v][color]:
        if u not in discovered[color] or length < discovered[color][u]:
            paths[u] = length if paths[u] == -1  else min(paths[u], length)
            discovered[color][u] = length
            dfs(u, pick_color(color), length + 1)


discovered = defaultdict(dict)
dfs(0, 'blue', 1)

discovered = defaultdict(dict)
dfs(0, 'red', 1)

print(paths)


G = DiGraph()
G.add_edges_from(red,label='red')
G.add_edges_from(blue,label='blue')
draw_networkx(G)
show()
