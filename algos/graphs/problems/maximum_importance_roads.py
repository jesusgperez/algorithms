from typing import List
from collections import defaultdict, deque
from algos.graphs.utils import visualize_undirected

edges = [[0,18],[18,1],[1,19],[21,20],[20,7],[7,8],[3,22],[22,13],[13,1],[13,9],[9,16],[16,7],[24,17],[17,3],[3,21],[22,6],[6,11],[11,7],[23,4],[4,15],[15,12],[5,7],[7,21],[21,1]]
# edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

# visualize_undirected(edges)
n = max((v for edge in edges for v in edge))
degree = [0 for _ in range(n + 1)]
weight = {}

for x,y in edges:
    degree[x] += 1
    degree[y] += 1

degree.sort()
print(sum((weight * deg for weight, deg in enumerate(degree, start=1))))
