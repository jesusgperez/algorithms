from math import inf
from utils import visualize_undirected

edges = [[0,1,5],[0,3,12],[0,2,7],[1,4,7],[1,2,9],[2,3,4],[2,4,4],[2,5,3],[3,5,7],[4,5,2],[4,6,5],[5,6,2]]
n = 0
for u, v, _ in edges: n = max(n, u, v)
n = n + 1

adj = [[inf if i != j else 0 for j in range(n)] for i in range(n)]

for u, v, w in edges:
    adj[u][v] = w
    adj[v][u] = w

print(adj)

for k in range(n):
    for i in range(n):
        for j in range(n):
            through_k = adj[i][k] + adj[k][j]
            if through_k < adj[i][j]:
                adj[i][j] = through_k

# visualize_undirected(edges, True)
print(adj)
