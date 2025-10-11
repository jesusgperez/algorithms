from typing import List

response = []

adj = [[1,4],[2,4],[3],[4],[]]

def dfs(v: int, path: List[int]):
    path.append(v)

    for u in adj[v]:
        dfs(u, path)

    if v == len(adj) - 1:
        response.append(path[:])

    path.pop()

dfs(0,[])

print(response)
