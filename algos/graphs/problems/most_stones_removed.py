from collections import defaultdict
from typing import Dict, List, Tuple

# stones = [[0,0],[0,1],[1,0],[2,0],[0,2],[2,2]]
stones = [[0,1],[1,0],[1,1]]

adj, x_coords, y_coords = defaultdict(list), defaultdict(list), defaultdict(list)
deps = defaultdict(int)

for x, y in stones:
    x_coords[x].append((x,y))
    y_coords[y].append((x,y))


def load_adj(coords: Dict[Tuple, List]):
    for coord in coords:
        current = coords[coord]
        prev = 0
        for i in range(1, len(current)):
            adj[current[prev]].append(current[i])
            adj[current[i]].append(current[prev])
            deps[current[i]] += 1
            prev = i

load_adj(x_coords)
load_adj(y_coords)

discovered, processed = set(), set()
times, parents = defaultdict(int), defaultdict(lambda: -1)
time, max_stones = 0, 0

def dfs(v: Tuple, root: Tuple):
    global time, max_stones
    time += 1
    discovered.add(v)
    times[v] = time

    for u in adj[v]:
        if u not in discovered:
            parents[u] = v
            dfs(u, root)

    max_stones = max(max_stones, times[v] - times[root])

for stone in stones:
    current = tuple(stone)
    if current not in discovered:
        dfs(current, current)

pass
