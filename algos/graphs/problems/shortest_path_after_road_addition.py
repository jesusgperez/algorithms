from typing import List
from collections import deque

queries = []
n = 500

adj = {i: [i + 1] for i in range(n)}

def bfs(adj: List):
    q = deque(((0, 0),))
    discovered = {0}

    while q:
        u, l = q.popleft()

        for v in adj[u]:
            if v == n - 1:
                return l + 1
            if v not in discovered:
                discovered.add(v)
                q.append((v, l + 1))

response = []
for u,v in queries:
    adj[u].append(v)
    response.append(bfs(adj))

print(response)