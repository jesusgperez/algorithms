from collections import defaultdict, deque

x, y = 1, 5
n = 5

adj = defaultdict(list)
adj[x].append(y)
adj[y].append(x)
for i in range(1, n):
    adj[i].append(i + 1)
    adj[i + 1].append(i)

distance = defaultdict(dict)

def bfs(start: int, root: int):
    q = deque(((start, 0),))
    distance[root][start] = 0
    
    while q:
        u, length = q.popleft()
        for v in adj[u]:    
            if v not in distance[root]:
                distance[root][v] = length + 1
                q.append((v, length + 1))


for u in range(1, n + 1):
    bfs(u, u)

print(distance)
response = [0 for _ in range(n)]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if distance[i][j] > 0:
            response[distance[i][j] - 1] += 2

print(response)
