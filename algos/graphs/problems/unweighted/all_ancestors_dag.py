from collections import defaultdict, deque
from algos.graphs.utils import visualize_directed

edges = [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]
# visualize_directed(edges)
n = max([v for edge in edges for v in edge])
adj = defaultdict(list)
ancestors = defaultdict(set)
in_degree = defaultdict(int)

for x,y in edges:
    adj[x].append(y)
    in_degree[y] += 1

queue = deque((v for v in range(n) if in_degree[v] == 0))

while queue:
    v = queue.popleft()
    for u in adj[v]:
        ancestors[u].add(v)
        ancestors[u].update(ancestors[v])
        in_degree[u] -= 1
        if in_degree[u] == 0:
            queue.append(u)

print([list(ancestors[v]) for v in range(n)])
