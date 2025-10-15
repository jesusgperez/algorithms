from collections import defaultdict

stones = [[0,0],[0,1],[1,0],[2,0],[0,2],[2,2]]

adj, x_coords, y_coords = defaultdict(list), defaultdict(list), defaultdict(list)


for x, y in stones:
    x_coords[x].append((x,y))
    y_coords[y].append((x,y))

for coord in x_coords:
    current = x_coords[coord]
    prev = 0
    for i in range(1, len(current)):
        adj[current[prev]].append(current[i])
        adj[current[i]].append(current[prev])
        prev = i

for coord in y_coords:
    current = y_coords[coord]
    prev = 0
    for i in range(1, len(current)):
        adj[current[prev]].append(current[i])
        adj[current[i]].append(current[prev])
        prev = i
