# from algos.graphs.utils import visualize_directed

edges = [-1,7,15,15,-1,4,16,2,16,7,11,6,10,4,9,1,14,-1]
edges = [4,4,8,-1,9,8,4,4,1,1]

# visualize_directed([[u, v] for u, v in enumerate(edges) if v != -1])
node1, node2 = 6, 5

if node1 == node2:
    print(node1)

path1, path2 = {node1: 0}, {node2: 0}
def dfs(v: int, path: set, length: int):
    discovered.add(v)

    u = edges[v] 
    if u != -1:
        if u not in discovered:
            path[u] = length
            dfs(u, path, length + 1)

discovered = set()
dfs(node1, path1, 1)
discovered= set()
dfs(node2, path2, 1)

if node2 in path1 and node1 in path2:
    if path1[node2] < path2[node1]:
        print(node2)
    elif path1[node2] > path2[node1]:
        print(node1)
    else:
        print(min(node1, node2))

min_length, min_node = 2 * len(edges), -1
for v in range(len(edges)):
    if v in path1 and v in path2 and max(path1[v],path2[v]) < min_length:
        min_length = max(path1[v],path2[v])
        min_node = v

print(min_node)
