from typing import List
from collections import defaultdict


equations = ['a==b', 'a!=b']
adj = defaultdict(list)


for equation in equations:
    if '==' in equation:
        x, y = equation.split('==')
        adj[x].append((y,'=='))
        adj[y].append((x,'=='))
    else:
        x, y = equation.split('!=')
        adj[x].append((y,'!='))
        adj[y].append((x,'!='))


edges, parents = defaultdict(str), defaultdict(lambda: -1)
discovered, processed = set(), set()


class ContradictionException(Exception):
    pass


def process_edge(v: str, u: str, rel: str):
    if (v,u) not in edges or edges[(v,u)] == rel: 
        edges[(v,u)] = rel
        edges[(u,v)] = rel
        return

    raise ContradictionException('')


def dfs(v: str):
    discovered.add(v)

    for u, rel in adj[v]:
        if u not in discovered:
            parents[u] = v
            discovered.add(u)
            process_edge(v, u, rel)
            dfs(u)
        elif u not in processed and parents[v] != u:
            process_edge(v, u, rel)

    processed.add(v)


dfs('a')
