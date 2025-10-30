from collections import defaultdict

n, k = 5, 1
invocations = [[1,2],[0,1],[3,2]]
# n, k = 5, 0
# invocations = [[1,2],[0,2],[0,1],[3,4]]
n, k = 3, 2
invocations = [[1,2],[0,1],[2,0]]

adj = defaultdict(list)

for u,v in invocations:
    adj[u].append(v)


suspicious = set()
discovered = set()
can_delete = True

def dfs(u: int, suspicion: bool = True):
    global can_delete
    if suspicion:
        suspicious.add(u)
    else:
        discovered.add(u)

    for v in adj[u]:
        if suspicion:
            if v not in suspicious:
                dfs(v, suspicion)
        else:
            if v in suspicious:
                can_delete = False
            if v not in discovered:
                dfs(v, suspicion)

dfs(k)

for u in range(n):
    if u not in suspicious:
        dfs(u, False)

if can_delete:
    print(list(discovered))

print(list(discovered.union(suspicious)))
