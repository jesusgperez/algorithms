# https://leetcode.com/problems/find-eventual-safe-states

graph = [[1],[2,3],[5],[0],[5],[],[]]
# graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# graph = [[],[0,2,3,4],[3],[4],[]]

discovered, processed = set(), set()
cycles = set()
safe = set()

def dfs(v: int):
    discovered.add(v)
    is_terminal = True

    for u in graph[v]:
        if u not in discovered:
            dfs(u)
        elif u not in processed:
            cycles.add(v)

        if u not in safe:
            is_terminal = False

        if u in cycles:
            cycles.add(v)

    if not v in cycles and is_terminal:
        safe.add(v)

    processed.add(v)

for v in range(len(graph)):
    if v not in discovered:
        dfs(v)

print(safe)
