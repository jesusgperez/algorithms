n = 3
edges = [[1,0],[1,2],[0,1]]

adj = [[] for _ in range(n)]
dependencies = [0 for _ in range(n)]
discovered = [False for _ in range(n)]
processed = [False for _ in range(n)]
has_cycle = False
schedule = []

for x, y in edges:
    adj[y].append(x)
    dependencies[x] += 1


def dfs(v: int):
    global has_cycle
    discovered[v] = True
    schedule.append(v)

    for u in adj[v]:
        if has_cycle:
            break

        if discovered[u] and not processed[u]:
            has_cycle = True
            break

        dependencies[u] -= 1
        if dependencies[u] == 0:
            dfs(u)

    processed[v] = True

for v in range(n):
    if has_cycle:
        break

    if not discovered[v] and dependencies[v] == 0:
        dfs(v)


if has_cycle or not all(processed):
    print([])
else:
    print(schedule)
