from typing import List

n = 8
edges = [[1,0],[2,1],[3,2],[3,4],[5,3],[6,7]]

adj = [[] for _ in range(n)]
dependencies = [0 for _ in range(n)]
discovered = [False for _ in range(n)]
processed = [False for _ in range(n)]

for x, y in edges:
    adj[y].append(x)
    dependencies[x] += 1

has_cycle = False

def dfs(v: int):
    global has_cycle

    if has_cycle:
        return

    discovered[v] = True

    for u in adj[v]:
        if has_cycle:
            return

        if discovered[u] and not processed[u]:
            has_cycle = True
            return

        dependencies[u] -= 1
        if dependencies[u] == 0:
            dfs(u)

    processed[v] = True


for i in range(n):
    if has_cycle:
        break

    if not discovered[i] and dependencies[i] == 0:
        dfs(i)

print(all(processed) and not has_cycle)
