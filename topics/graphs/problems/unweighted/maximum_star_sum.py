from collections import defaultdict, deque

edges = [[3,1],[5,1],[0,3],[4,6],[1,4],[3,4],[6,3],[2,6],[5,2],[1,6],[6,0],[2,3],[3,5],[2,1],[0,2],[5,0],[0,4]] 
k = 6
vals = [17,49,-34,-17,-7,-23,24]

adj = defaultdict(list)
n = 0
for x,y in edges:
    adj[x].append(vals[y])
    adj[y].append(vals[x])
    n = max(x,y,n)

max_sum = min(vals)
discovered = set()

for v in range(n):
    current = sum(filter(lambda x: x > 0, sorted(adj[v], reverse=True)[:k])) + vals[v]
    max_sum = max(current, max_sum)    

print(max_sum)