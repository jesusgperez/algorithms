from typing import List


dislikes = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
n = 10

adj = [[] for _ in range(n + 1)]
parents = [-1 for _ in range(n + 1)]

for x, y in dislikes:
    adj[x].append(y)
    adj[y].append(x)

discovered, processed = set(), set()
cycles = []


def find_path(start: int, end: int, cycle: List[int]):
    if start == end or end == -1:
        cycle.append(end)
    else:
        find_path(start, parents[end], cycle)
        cycle.append(end)


def dfs(v: int):
    discovered.add(v)

    for u in adj[v]:
        if u not in discovered:
            discovered.add(u)
            parents[u] = v
            dfs(u)
        elif u not in processed and parents[v] != u:
            cycle = []
            find_path(u, v, cycle)
            cycles.append(cycle)

    processed.add(v)


for v in range(n + 1):
    if v not in discovered:
        dfs(v)


pass
