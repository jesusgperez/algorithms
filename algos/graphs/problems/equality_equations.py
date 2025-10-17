from typing import List
from collections import defaultdict


equations = ['a==b', 'b!=c', 'a!=c', 'c==d', 'e==b', 'd!=e', 'e==f', 'b==f', 'c!=g', 'd==g']
adj = defaultdict(dict)
letters = set()


class ContradictionException(Exception):
    pass


def add_edge(equation: str, rel: str):
    a, b = equation.split(rel)
    letters.add(a)
    letters.add(b)
    if b in adj[a] or a in adj[b]:
        raise ContradictionException
    adj[a][b] = rel
    adj[b][a] = rel


for equation in equations:
    if '==' in equation:
        add_edge(equation, '==')
    else:
        add_edge(equation, '!=')


parents = defaultdict(lambda: -1)
discovered, processed = set(), set()
differences = defaultdict(int)

def find_path(start:str, end: str):
    if start == end or parents[end] == -1:
        print(end)
    else:
        find_path(start, parents[end])
        print(end)


def dfs(v: str, diff: int):
    discovered.add(v)

    for u, rel in adj[v].items():
        if u not in discovered:
            diff += (rel == '!=')
            differences[u] = diff - differences[v]
            parents[u] = v
            discovered.add(u)
            dfs(u, diff)
            diff -= (rel == '!=')
        elif not processed and parents[v] != u:
            if diff == 0 and rel == '!=':
                raise ContradictionException('')

    processed.add(v)

has_contradiction = False

for l in letters:
    if l not in discovered:
        try:
            dfs('a', 0)
        except ContradictionException as e:
            has_contradiction = True
            break


print(has_contradiction)
