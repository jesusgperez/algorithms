from typing import List
from pydantic import BaseModel
from collections import defaultdict

dislikes = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
n = 10

class Info(BaseModel):
    discovered: bool = False
    processed: bool = False
    parent: int = -1
    entry: int = 0

info = defaultdict(Info)

adj = [[] for _ in range(n + 1)]

for x, y in dislikes:
    adj[x].append(y)
    adj[y].append(x)

time_delta = []
time = 0

# If there are cycles of odd length, then bipartition cannot be reached
def dfs(v: int):
    global time
    time += 1
    info[v].discovered = True
    info[v].entry = time

    for u in adj[v]:
        if not info[u].discovered:
            info[u].discovered = True
            info[u].parent = v
            dfs(u)
        elif not info[u].processed and info[v].parent != u:
            time_delta.append(info[v].entry - info[u].entry)

    time += 1
    info[v].processed = True


for v in range(n + 1):
    if not info[v].discovered:
        dfs(v)

pass
