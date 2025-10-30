from collections import deque
from networkx import draw_networkx, Graph
from matplotlib.pyplot import show

n_vertices = 30
edges = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4],[2,5],[2,6],[3,6],[5,6],[3,5]]
# edges = [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]
# edges = [[8,7],[26,19],[23,8],[19,17],[29,25],[16,6],[8,15],[13,23],[1,28],[19,27],[9,30],[7,28],[30,4],[15,12],[1,10],[10,3],[18,28],[9,20],[13,1],[26,3],[24,29],[10,6],[3,23],[27,14],[13,24],[21,16],[17,30],[21,26],[16,18],[6,4],[4,7],[27,2],[2,5],[14,22],[29,14],[25,5]]
# edges = [[1,2],[7,3],[3,1],[7,2],[2,3],[6,1],[4,8],[4,6],[5,7],[4,5]]
edges = [[27,30],[17,5],[22,21],[18,11],[26,16],[11,6],[9,6],[6,18],[11,19],[25,2],[12,30],[13,28],[24,10],[7,12],[18,15],[5,13],[27,23],[24,30],[24,3],[14,4],[12,17],[9,29],[10,8],[28,1],[23,8],[25,15],[19,1],[8,27],[9,5],[4,21],[14,15],[10,22],[16,7],[28,29],[2,29],[19,25],[2,17],[26,1],[3,20]]

adj = [[] for _ in range(n_vertices + 1)]
colors = [0 for _ in range(n_vertices + 1)]

for x, y in edges:
    adj[x].append(y)
    adj[y].append(x)

discovered, processed = set(), set()

def process_edge(v: int, u: int):
    if colors[u] == 0:
        colors[u] = colors[v] % 4 + 1
    elif colors[u] == colors[v]:
        possible = {1,2,3,4}
        for w in adj[u]:
            possible.discard(colors[w])
        colors[u] = list(possible)[0]

def bfs(start: int):
    queue = deque((start,))
    discovered.add(start)
    colors[start] = 1

    while queue:
        v = queue.popleft()
        for u in adj[v]:
            if u not in processed:
                process_edge(v, u)

            if u not in discovered:
                discovered.add(u)
                queue.append(u)

        processed.add(v)

bfs(1)

print(colors)

discovered, processed = set(), set()

def detect(start: int):
    queue = deque((start,))
    discovered.add(start)

    while queue:
        v = queue.popleft()
        for u in adj[v]:
            if u not in processed:
                if colors[u] == colors[v]:
                    print(v,'->',u)

            if u not in discovered:
                discovered.add(u)
                queue.append(u)

        processed.add(v)

detect(1)

G = Graph()
G.add_edges_from(edges)
draw_networkx(G)
show()
