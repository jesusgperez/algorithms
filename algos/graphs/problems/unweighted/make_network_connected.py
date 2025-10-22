from collections import defaultdict

connections = [[0,1],[0,2],[1,2]]
n = 4

adj = defaultdict(list)
parent = defaultdict(lambda: -1)

for x,y in connections:
    adj[x].append(y)
    adj[y].append(x)

discovered, processed = set(), set()
back_edges = 0

def dfs(v: int):
    global back_edges
    discovered.add(v)

    for u in adj[v]:
        if u not in discovered:
            parent[u] = v
            dfs(u)
        elif u not in processed and parent[v] != u:
            back_edges += 1

    processed.add(v)

components = 0

for v in range(n):
    if v not in discovered:
        components += 1
        dfs(v)

print(back_edges >= components - 1)

